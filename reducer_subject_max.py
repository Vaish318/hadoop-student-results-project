#!/usr/bin/env python3
import sys
cur = None
best_name=None
best_marks=-999999
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    parts=line.split("\t",1)
    if len(parts)!=2: continue
    subj,val=parts
    name,marks = val.rsplit("|",1)
    try: m=int(marks)
    except: continue
    if cur is None:
        cur=subj
        best_name=name; best_marks=m
    elif subj!=cur:
        print(f"{cur}\t{best_name}\t{best_marks}")
        cur=subj; best_name=name; best_marks=m
    else:
        if m>best_marks:
            best_marks=m; best_name=name
if cur is not None:
    print(f"{cur}\t{best_name}\t{best_marks}")
