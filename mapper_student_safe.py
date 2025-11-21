#!/usr/bin/env python3
import sys, traceback

def safe_print(s):
    try:
        sys.stdout.write(s+"\n")
    except:
        pass

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    if line.startswith("student_id"): continue
    parts = line.split(",")
    if len(parts) < 5: continue

    sid = parts[0].strip()
    name = parts[1].strip()

    try:
        marks = int(parts[4].strip())
    except:
        continue

    safe_print(f"{sid}|{name}\t{marks}")
