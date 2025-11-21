# README.md

````markdown
# Hadoop Student Results — Analytics & MapReduce

**Short description**
A small Hadoop Streaming project that generates synthetic student marks, runs streaming MapReduce jobs to compute per-subject statistics and per-student totals, and analyzes results using Jupyter/Pandas and visualizations.

**Contents**
- Mapper & reducer scripts for subject-level and student-level MapReduce jobs
- `student_marks.csv` synthetic dataset generator
- Jupyter notebooks with data analysis and plots
- `run.sh` helper to run common HDFS + streaming steps

## Prerequisites
- macOS / Linux
- Java JDK 1.8+ (for Hadoop)
- Hadoop (single-node pseudo-distributed) installed and configured
- Python 3.8+ with packages: pandas, matplotlib, numpy, seaborn (optional), jupyter
- `hdfs`, `hadoop`, `yarn` CLI available in PATH
- Git (and optionally `git-lfs` if you want to store big files)

## Quick project layout
```text
hadoop-student-results/
├─ mapper_subject.py
├─ reducer_subject.py
├─ mapper_student_safe.py
├─ reducer_student.py
├─ student_marks.csv         # (OPTIONAL: large - tracked in .gitignore)
├─ generate_data.py         # script to generate synthetic dataset
├─ run.sh                   # convenience script to upload & run jobs
├─ notebooks/
│  └─ Hadoop_student_results_notebook.ipynb
├─ results/
│  └─ subject_stats.txt
├─ plots/
│  └─ histogram_totals.png
├─ top50_students.csv
└─ README.md
````

## How to run (high level)

1. Start Hadoop (NameNode, DataNode, ResourceManager, NodeManager) in pseudo-distributed mode.
2. Upload data to HDFS:

   ```bash
   hdfs dfs -mkdir -p /user/$USER/student_data
   hdfs dfs -put -f student_marks.csv /user/$USER/student_data/
   ```
3. Run Hadoop streaming job (example — subject stats):

   ```bash
   STREAMING_JAR=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar
   hadoop jar "$STREAMING_JAR" \
     -files mapper_subject.py,reducer_subject.py \
     -mapper mapper_subject.py \
     -reducer reducer_subject.py \
     -numReduceTasks 2 \
     -input /user/$USER/student_data/student_marks.csv \
     -output /user/$USER/output_subject_stats
   hdfs dfs -cat "/user/$USER/output_subject_stats/part-*"
   ```
4. Pull outputs to local, analyze in Jupyter, plot charts, export CSVs.

## Jupyter analysis

* `notebooks/Hadoop_student_results_notebook.ipynb` demonstrates how to:

  * read HDFS output into pandas using `subprocess` calls to `hdfs dfs -cat`
  * pivot, grade, compute percentiles
  * produce histogram, bar charts, correlation heatmap


* Include the notebook (with outputs) and `run.sh` showing commands you ran.
* Mark large datasets as omitted and mention how to regenerate them with `generate_data.py`.

---

````

---

# .gitignore

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.env/*
venv/
.envrc
.venv/

# Jupyter
.ipynb_checkpoints/
*.ipynb

# OS
.DS_Store
Thumbs.db

# Data / results (do not store huge CSVs / binary outputs in git)
student_marks.csv
results/
plots/
*.png
*.jpg
*.jpeg
*.parquet
*.bin

# Hadoop temporary / outputs
output_*/
/user/*/output_*

# Git LFS pointer files (if using LFS)
.gitattributes

# logs
*.log

# local hadoop / temp
/tmp/*

# keep README, small example CSVs and scripts tracked
!README.md
!generate_data.py
!run.sh
````

---

# Branch setup & workflow (recommended)

````markdown
# Branching & workflow
Use a simple GitHub flow for your project:

- `main` — stable notebook & final deliverables. (protected branch for final submission)
- `dev` — active development branch where you merge feature branches.
- `feature/<name>` — one feature per branch (e.g. `feature/hive-integration`, `feature/visualizations`)

Typical workflow:
1. `git checkout -b feature/visualizations dev`
2. Make changes, test locally and in notebook.
3. Commit with meaningful messages:
   - `git add modified_file.py`
   - `git commit -m "Add correlation heatmap and subject averages plot"`
4. Push and open a Pull Request against `dev`.
5. Merge PR into `dev` after review, then merge `dev` into `main` for release.

Tagging & releases:
- When you are ready to submit to the examiner, merge `dev` to `main` and tag a release:
  ```bash
  git checkout main
  git merge dev
  git tag -a v1.0 -m "Exam submission v1.0"
  git push origin main --tags
````

````

---

# Recommended repo structure and small explanations

```text
hadoop-student-results/                # repo root
├─ data/                               # *optional* small sample datasets (safe to commit)
│  └─ sample_student_marks_small.csv
├─ scripts/                            # small helper scripts
│  ├─ generate_data.py                 # generates synthetic dataset
│  ├─ run.sh                           # orchestrates HDFS + streaming jobs
│  └─ collect_results.sh               # fetch outputs from HDFS and prepare CSVs
├─ hadoop/                             # streaming mappers & reducers
│  ├─ mapper_subject.py
│  ├─ reducer_subject.py
│  ├─ mapper_student_safe.py
│  └─ reducer_student.py
├─ notebooks/
│  └─ Hadoop_student_results_notebook.ipynb
├─ results/                            # (ignored in git by default) final outputs
│  ├─ subject_stats.txt
│  └─ student_totals_graded.csv
├─ plots/                              # (ignored) plots generated by notebook/scripts
├─ README.md
├─ .gitignore
└─ LICENSE
````

**Why separate `scripts/` and `hadoop/`?**

* `hadoop/` holds streaming mappers/reducers which are the core MapReduce logic. `scripts/` contains orchestration utilities helpful for demoing the pipeline.

---

# Small `run.sh` template (copy into `scripts/run.sh` and mark executable)

```bash
#!/usr/bin/env bash
set -euo pipefail
USER=${USER:-$(whoami)}
HDFS_DIR=/user/$USER/student_data
LOCAL_CSV=student_marks.csv
HADOOP_STREAMING_JAR=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar

# upload data
hdfs dfs -mkdir -p $HDFS_DIR
hdfs dfs -put -f $LOCAL_CSV $HDFS_DIR/

# run subject stats job
hadoop jar $HADOOP_STREAMING_JAR \
  -files hadoop/mapper_subject.py,hadoop/reducer_subject.py \
  -mapper hadoop/mapper_subject.py \
  -reducer hadoop/reducer_subject.py \
  -numReduceTasks 2 \
  -input $HDFS_DIR/$LOCAL_CSV \
  -output /user/$USER/output_subject_stats

# fetch results
hdfs dfs -cat "/user/$USER/output_subject_stats/part-*" > results/subject_stats.txt

# (add other jobs as needed)
```

