# Multiprocessing

## What is it?
A way to run multiple tasks **truly in parallel** by spawning separate Python processes — each with its own memory and CPU core.

---

## Why does it exist?
Python has a limitation called the **GIL (Global Interpreter Lock)** — it allows only one thread to execute Python code at a time. This means multithreading in Python **cannot use multiple CPU cores** for CPU-heavy work.

Multiprocessing bypasses the GIL entirely by spawning **separate processes** instead of threads. Each process gets its own Python interpreter and memory space, so they run on different CPU cores **simultaneously**.

> Without multiprocessing: 4 heavy tasks run one after another → slow.
> With multiprocessing: 4 heavy tasks run on 4 cores at the same time → ~4x faster.

---

## Where is it used?

| Domain | Real-world use |
|---|---|
| Data Engineering | Parsing and transforming large CSV/JSON files in parallel |
| ML Engineering | Parallel hyperparameter tuning, data preprocessing pipelines |
| Data Science | Running simulations or bootstrapping across large datasets |
| Backend Engineering | CPU-intensive request handling (e.g. image/video processing) |

**Real companies/tools using this pattern:**
- **Scikit-learn** uses `n_jobs=-1` which internally uses multiprocessing
- **Apache Spark** (local mode) spawns worker processes per partition
- **Celery** (task queues) distributes CPU tasks across worker processes
- **Gunicorn** (Python web server) spawns multiple worker processes

---

## Which job roles ask for this?
- `Data Engineer` — parallel file ingestion, ETL pipeline optimization
- `ML Engineer` — fast data preprocessing, distributed training prep
- `Data Scientist` — parallel model evaluation, simulation
- `Backend Engineer` — offloading CPU-bound tasks from the main thread

---

## The Core Idea (Visual)
```
WITHOUT multiprocessing (sequential):
Core 1: [Task 1]──[Task 2]──[Task 3]──[Task 4]   ← slow

WITH multiprocessing (parallel):
Core 1: [Task 1]
Core 2: [Task 2]
Core 3: [Task 3]
Core 4: [Task 4]  ← all finish at roughly the same time
```

---

## Code Example
See `demo.py` in this folder. The demo shows three things:
1. Running a CPU-heavy task **sequentially** (slow)
2. Running the same task using **multiprocessing** (fast)
3. Using **Pool.map()** — the most common real-world pattern

---

## Output
```
============================================================
 MULTIPROCESSING DEMO
============================================================

[1] SEQUENTIAL EXECUTION
------------------------------------------------------------
Running 4 tasks one after another on a single core...
  Task 1 done in 2.01s
  Task 2 done in 2.01s
  Task 3 done in 2.01s
  Task 4 done in 2.01s
Total sequential time: 8.06s

[2] MULTIPROCESSING EXECUTION
------------------------------------------------------------
Running 4 tasks in parallel across multiple cores...
  Task 3 done in 2.02s  (worker pid: 45231)
  Task 1 done in 2.02s  (worker pid: 45229)
  Task 4 done in 2.02s  (worker pid: 45232)
  Task 2 done in 2.02s  (worker pid: 45230)
Total multiprocessing time: 2.04s

Speedup: 3.95x faster

[3] POOL.MAP() — THE REAL-WORLD PATTERN
------------------------------------------------------------
Processing a dataset of 8 chunks in parallel...
  Chunk 0: 10000 rows processed
  Chunk 1: 10000 rows processed
  ...
All chunks done in 1.03s
Total rows processed: 80000
```

---

## Key Takeaways
- Use multiprocessing for **CPU-bound** tasks (number crunching, data transformation, model training prep)
- Use multithreading for **I/O-bound** tasks (API calls, file reads, database queries)
- `Pool.map()` is the cleanest pattern for applying a function to a list of inputs in parallel

---

## When NOT to use it
- **I/O-bound tasks** — use threading or async instead
- **Shared mutable state** — processes don't share memory
- **Very short tasks** — spawning processes has overhead

---

## Related Concepts
- `multithreading/` — parallelism for I/O-bound tasks, limited by GIL
- `concurrent.futures/` — cleaner unified API over both threading and multiprocessing
- `dask/` — multiprocessing scaled to datasets larger than RAM
- `ray/` — multiprocessing scaled to clusters with fault tolerance
