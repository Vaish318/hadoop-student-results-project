#!/usr/bin/env python3
import sys
current = None
min_name = None
min_marks = 10**9
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    parts=line.split("\t",1)
    if len(parts)!=2: continue
    subject,val=parts
    try:
        name,marks = val.rsplit("|",1)
        marks = int(marks)
    except:
        continue
    if current is None:
        current, min_name, min_marks = subject, name, marks
    elif subject != current:
        print(f"{current}\t{min_name}\t{min_marks}")
        current, min_name, min_marks = subject, name, marks
    else:
        if marks < min_marks:
            min_marks = marks
            min_name = name
if current is not None:
    print(f"{current}\t{min_name}\t{min_marks}")
