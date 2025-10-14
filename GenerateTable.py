# Python snippet — save and run on your machine to populate the table
# It updates ChronologicalOrder.md between the <!-- FILE_TABLE_START --> and <!-- FILE_TABLE_END --> markers.

import os, datetime, re

root = r"c:\GitHub\2BCA-A"
md_file = os.path.join(root, "ChronologicalOrder.md")

py_files = []
for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        if f.lower().endswith(".py"):
            full = os.path.join(dirpath, f)
            mtime = os.path.getmtime(full)
            rel = os.path.relpath(full, root).replace("\\", "/")
            py_files.append((mtime, rel))

# Sort by mtime (oldest first). Use reverse=True in sort() for newest-first.
py_files.sort()

lines = [
    "<!-- FILE_TABLE_START -->",
    "| Date modified | File |",
    "|---|---|"
]

for mtime, rel in py_files:
    # changed: format date as DD-MM-YYYY and 12-hour time with AM/PM
    dt = datetime.datetime.fromtimestamp(mtime).strftime("%d-%m-%Y %I:%M:%S %p")
    url = "https://github.com/AlanBennyOfficial/2BCA-A/blob/main/" + rel
    name = os.path.basename(rel)
    lines.append(f"| {dt} | [{rel}]({url}) |")

lines.append("<!-- FILE_TABLE_END -->")

with open(md_file, "r", encoding="utf-8") as f:
    s = f.read()

new = re.sub(r"<!-- FILE_TABLE_START -->.*?<!-- FILE_TABLE_END -->", "\n".join(lines), s, flags=re.S)

with open(md_file, "w", encoding="utf-8") as f:
    f.write(new)

print("Chronological table updated in", md_file)