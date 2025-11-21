#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # skip header line if present in any split
    if line.startswith("student_id,") or line.lower().startswith("student_id,"):
        continue
    parts = line.split(",")
    if len(parts) < 5:
        continue
    subject = parts[3].strip()
    try:
        marks = int(parts[4].strip())
    except:
        continue
    print(f"{subject}\t{marks}")


