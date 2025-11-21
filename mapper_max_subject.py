#!/usr/bin/env python3
import sys, csv
r = csv.DictReader(sys.stdin)
for row in r:
    try:
        subject = row['subject'].strip()
        name = row['name'].strip()
        marks = int(row['marks'])
        print(f"{subject}\t{name}|{marks}")
    except Exception:
        continue
