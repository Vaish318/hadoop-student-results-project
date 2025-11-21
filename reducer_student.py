#!/usr/bin/env python3
import sys

current = None
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t", 1)
    if len(parts) != 2:
        continue
    
    key, val = parts
    try:
        marks = int(val)
    except:
        continue

    if current is None:
        current = key
        total = 0

    if key != current:
        sid, name = current.split("|", 1)
        print(f"{sid}\t{name}\t{total}")
        current = key
        total = 0

    total += marks

if current is not None:
    sid, name = current.split("|", 1)
    print(f"{sid}\t{name}\t{total}")
