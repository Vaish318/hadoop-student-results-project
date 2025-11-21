import csv
import matplotlib.pyplot as plt

# histogram of totals
totals = []
with open("student_totals_fixed.txt","r") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            try:
                totals.append(float(parts[2]))
            except:
                continue

if totals:
    plt.figure()
    plt.hist(totals, bins=20)
    plt.title("Histogram of student totals")
    plt.xlabel("Total marks")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.savefig("histogram_totals.png")
    plt.close()

# average per subject (reads student_marks.csv)
subject_sum = {}
subject_count = {}
try:
    with open("student_marks.csv","r") as f:
        reader = csv.DictReader(f)
        for r in reader:
            subj = r.get("subject") or ""
            try:
                m = float(r.get("marks",0))
            except:
                continue
            subject_sum.setdefault(subj,0.0)
            subject_count.setdefault(subj,0)
            subject_sum[subj] += m
            subject_count[subj] += 1
except FileNotFoundError:
    subject_sum = {}
    subject_count = {}

if subject_sum:
    subjects = sorted(subject_sum.keys())
    avgs = [ subject_sum[s]/subject_count[s] for s in subjects ]
    plt.figure()
    plt.bar(subjects, avgs)
    plt.title("Average marks per subject")
    plt.xlabel("Subject")
    plt.ylabel("Average marks")
    plt.tight_layout()
    plt.savefig("subject_avg_bar.png")
    plt.close()
