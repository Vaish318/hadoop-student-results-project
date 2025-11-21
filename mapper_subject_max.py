#!/usr/bin/env python3
import sys, csv
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    if line.lower().startswith("student_id,"): continue
    parts=line.split(",")
    if len(parts) < 5: continue
    subj = parts[3].strip()
    name = parts[1].strip()
    try:
        marks = int(parts[4].strip())
    except:
        continue
    # emit subject \t name|marks
    print(f"{subj}\t{name}|{marks}")
