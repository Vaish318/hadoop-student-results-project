#!/usr/bin/env python3
import sys
current=None
count=0
total=0
pass_count=0
for line in sys.stdin:
    line=line.strip()
    if not line: continue
    parts=line.split("\t",1)
    if len(parts)!=2: continue
    subj, val = parts
    try:
        marks = int(val)
    except:
        continue
    if current is None:
        current = subj; count=0; total=0; pass_count=0
    if subj != current:
        avg = total/count if count else 0
        pct_pass = (pass_count/count*100) if count else 0
        print(f"{current}\t{count}\t{total}\t{avg:.2f}\t{pct_pass:.2f}")
        current = subj; count=0; total=0; pass_count=0
    count += 1
    total += marks
    if marks >= 40:
        pass_count += 1
if current is not None:
    avg = total/count if count else 0
    pct_pass = (pass_count/count*100) if count else 0
    print(f"{current}\t{count}\t{total}\t{avg:.2f}\t{pct_pass:.2f}")
