#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    if line.startswith("student_id,") or line.lower().startswith("student_id,"): continue
    parts = line.split(",")
    if len(parts) < 5: continue
    sid = parts[0].strip()
    name = parts[1].strip()
    try: marks = int(parts[4].strip())
    except: continue
    print(f"{sid}|{name}\\t{marks}")
