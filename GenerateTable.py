# Python snippet — save and run on your machine to populate the table
# It updates ChronologicalOrder.md between the <!-- FILE_TABLE_START --> and <!-- FILE_TABLE_END --> markers.

import os, datetime, re

root = r"c:\GitHub\2BCA-A"
html_file = os.path.join(root, "ChronologicalOrder.html")

py_files = []
for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        if f.lower().endswith(".py"):
            full = os.path.join(dirpath, f)
            mtime = os.path.getmtime(full)
            rel = os.path.relpath(full, root).replace("\\", "/")
            py_files.append((mtime, rel))

# Sort by mtime (oldest first).
py_files.sort()

# Build HTML
lines = []
lines.append("<!-- AUTO-GENERATED: ChronologicalOrder.html -->")
lines.append("<!doctype html>")
lines.append("<html lang='en'>")
lines.append("<head>")
lines.append("  <meta charset='utf-8'/>")
lines.append("  <meta name='viewport' content='width=device-width,initial-scale=1'/>")
lines.append("  <title>DSP Python Programs ordered chronologically</title>")
lines.append("  <style>")
lines.append("    table{border-collapse:collapse;width:100%}")
lines.append("    th,td{border:1px solid #ddd;padding:8px;text-align:left}")
lines.append("    th{background:#f4f4f4}")
lines.append("  </style>")
lines.append("</head>")
lines.append("<body>")
lines.append("<h1>DSP Python Programs ordered chronologically</h1>")
lines.append("<p> </p>")
lines.append("<table>")
lines.append("  <thead><tr><th>Date modified</th><th>File</th></tr></thead>")
lines.append("  <tbody>")

for mtime, rel in py_files:
    # format date as DD-MM-YYYY and 12-hour time with AM/PM
    dt = datetime.datetime.fromtimestamp(mtime).strftime("%d-%m-%Y %I:%M:%S %p")
    url = "https://github.com/AlanBennyOfficial/2BCA-A/blob/main/" + rel
    lines.append(f"  <tr><td>{dt}</td><td><a href=\"{url}\">{rel}</a></td></tr>")

lines.append("  </tbody>")
lines.append("</table>")
lines.append("</body>")
lines.append("</html>")

with open(html_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Chronological HTML table written to", html_file)