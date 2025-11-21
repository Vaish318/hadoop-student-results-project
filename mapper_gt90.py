#!/usr/bin/env python3
import sys, csv
r = csv.DictReader(sys.stdin)
for row in r:
    try:
        subj = row['subject'].strip()
        marks = int(row['marks'])
        if marks > 90:
            print(f"{subj}\t1")
    except:
        continue
