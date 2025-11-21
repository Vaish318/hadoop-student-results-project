#!/usr/bin/env python3
import sys
current=None
total=0
count=0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    parts=line.split("\t",1)
    if len(parts)!=2: continue
    key,val=parts
    try:
        marks = int(val)
    except:
        continue
    if current is None:
        current = key; total=0; count=0
    if key != current:
        sid,name = current.split("|",1)
        avg = total/count if count else 0
        if avg > 75: cat='Strong'
        elif avg >= 50: cat='Average'
        else: cat='Weak'
        print(f"{sid}\t{name}\t{total}\t{count}\t{avg:.2f}\t{cat}")
        current = key; total=0; count=0
    total += marks
    count += 1
if current is not None:
    sid,name = current.split("|",1)
    avg = total/count if count else 0
    if avg > 75: cat='Strong'
    elif avg >= 50: cat='Average'
    else: cat='Weak'
    print(f"{sid}\t{name}\t{total}\t{count}\t{avg:.2f}\t{cat}")
