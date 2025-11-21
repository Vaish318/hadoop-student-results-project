#!/usr/bin/env python3
import sys, csv
r = csv.DictReader(sys.stdin)
for row in r:
    try:
        sid = row['student_id'].strip()
        name = row['name'].strip()
        marks = int(row['marks'])
        print(f"{sid}|{name}\t{marks}")
    except:
        continue
