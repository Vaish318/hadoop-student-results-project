#!/usr/bin/env python3
import sys

current_subject = None
count = 0
total = 0
maximum = None

def emit(subject, count, total, maximum):
    avg = total / count if count else 0
    print(f"{subject}\t{count}\t{total}\t{maximum}\t{avg:.2f}")

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    parts = line.split("\t",1)
    if len(parts) != 2: continue
    subject, val = parts
    try:
        marks = int(val)
    except:
        continue
    if current_subject is None:
        current_subject = subject
        count = 0
        total = 0
        maximum = marks
    if subject != current_subject:
        emit(current_subject, count, total, maximum)
        current_subject = subject
        count = 0
        total = 0
        maximum = marks
    count += 1
    total += marks
    if maximum is None or marks > maximum:
        maximum = marks

if current_subject is not None:
    emit(current_subject, count, total, maximum)
