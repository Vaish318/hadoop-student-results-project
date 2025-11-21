#!/usr/bin/env python3
import sys
current = None
best_name = None
best_marks = -1
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    parts = line.split("\t",1)
    if len(parts)!=2: continue
    subject, val = parts
    try:
        name, marks = val.rsplit("|",1)
        marks = int(marks)
    except:
        continue
    if current is None:
        current = subject
        best_name = name
        best_marks = marks
    if subject != current:
        print(f"{current}\t{best_name}\t{best_marks}")
        current, best_name, best_marks = subject, name, marks
    else:
        if marks > best_marks:
            best_marks = marks
            best_name = name
if current is not None:
    print(f"{current}\t{best_name}\t{best_marks}")
