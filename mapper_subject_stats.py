#!/usr/bin/env python3
import sys, csv
r = csv.DictReader(sys.stdin)
for row in r:
    try:
        subject = row['subject'].strip()
        marks = int(row['marks'])
        print(f"{subject}\t{marks}")
    except:
        continue
