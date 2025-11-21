#!/usr/bin/env python3
import sys
current = None
count = 0
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    subject, marks = line.split("\t")
    marks = int(marks)

    if current is None:
        current = subject

    if subject != current:
        print(f"{current}\t{count}\t{total}\t{100}\t{total/count}")
        current = subject
        count = 0
        total = 0

    count += 1
    total += marks

if current is not None:
    print(f"{current}\t{count}\t{total}\t{100}\t{total/count}")
