#!/usr/bin/env python3
import sys
current=None
total=0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    parts=line.split("\t",1)
    if len(parts)!=2: continue
    subj,val=parts
    try:
        v=int(val)
    except:
        continue
    if current is None:
        current=subj; total=0
    if subj != current:
        print(f"{current}\t{total}")
        current=subj; total=0
    total += v
if current is not None:
    print(f"{current}\t{total}")
