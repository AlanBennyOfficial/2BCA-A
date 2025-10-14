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
lines.append('  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">')
lines.append("  <style>")
lines.append("    :root{--bg:#f6f8fa;--card:#ffffff;--muted:#6b7280;--accent:#2563eb;--border:rgba(15,23,42,0.06)}")
lines.append("    html,body{height:100%}")
lines.append("    body{margin:0;font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;background:var(--bg);color:#0f172a;padding:32px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}")
lines.append("    .container{max-width:1100px;margin:0 auto}")
lines.append("    .card{background:var(--card);border-radius:12px;box-shadow:0 6px 18px rgba(15,23,42,0.06);padding:20px;border:1px solid var(--border);overflow:auto}")
lines.append("    h1{margin:0 0 8px;font-weight:600} p.lead{margin:0 0 18px;color:var(--muted);font-size:0.95rem}")
lines.append("    table{width:100%;border-collapse:separate;border-spacing:0;font-size:0.95rem;min-width:640px}")
lines.append("    thead th{ text-align:left;padding:12px 14px;background:linear-gradient(180deg,rgba(249,250,251,0.8),rgba(243,244,246,0.8));font-weight:600;color:#0f172a;border-bottom:1px solid var(--border);position:sticky;top:0;-webkit-backdrop-filter: blur(6px);backdrop-filter: blur(6px);}")
lines.append("    tbody td{padding:12px 14px;border-bottom:1px dashed var(--border);vertical-align:middle}")
lines.append("    tbody tr:nth-child(even){background:rgba(15,23,42,0.02)} tbody tr:hover{background:rgba(37,99,235,0.04)}")
lines.append("    a.file-link{color:var(--accent);text-decoration:none;font-weight:500} .time{color:var(--muted);font-variant-numeric:tabular-nums}")
lines.append("    @media (max-width:720px){body{padding:18px} table{font-size:0.88rem} thead th, tbody td{padding:10px 8px}}")
lines.append("  </style>")
lines.append("</head>")
lines.append("<body>")
lines.append("<div class='container'><div class='card'>")
lines.append("<h1>DSP Python Programs ordered chronologically</h1>")
lines.append("<p> </p>")
lines.append("<table>")
lines.append("  <thead><tr><th>Date modified</th><th>File</th></tr></thead>")
lines.append("  <tbody>")

for mtime, rel in py_files:
    # format date as DD-MM-YYYY and 12-hour time with AM/PM
    dt = datetime.datetime.fromtimestamp(mtime).strftime("%d-%m-%Y %I:%M:%S %p")
    url = "https://github.com/AlanBennyOfficial/2BCA-A/blob/main/" + rel
    # changed: include data-label attributes for responsive stacking on mobile
    lines.append(f"  <tr><td class='time' data-label=\"Date modified\">{dt}</td><td data-label=\"File\"><a class='file-link' href=\"{url}\">{rel}</a></td></tr>")

lines.append("  </tbody>")
lines.append("</table>")
lines.append("</div></div>")
lines.append("</body>")
lines.append("</html>")

with open(html_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Chronological HTML table written to", html_file)