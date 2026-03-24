# tech-concepts-decoded

> Every concept a job description throws at you — explained plainly, with code and real output.

Job postings list buzzwords. Nobody explains *why* they matter or *where* they're actually used.  
This repo fixes that. Each concept follows the same structure:
```
What is it → Why it exists → Where it's used → Which roles need it → Code → Output → Takeaways
```

---

## Who is this for?

Students and early-career folks preparing for roles in:
- **Data Engineering**
- **ML Engineering**
- **Data Science**
- **Backend / Software Engineering**

---

## How to use this repo

1. See a term in a job description you don't understand
2. Find it in the index below
3. Read the README → run the demo → understand it for real

---

## Concept Index

### Concurrency & Distributed Computing

| Concept | What it solves | Relevant Roles |
|---|---|---|
| [Multiprocessing](concepts/concurrency/multiprocessing/README.md) | CPU-bound parallelism, bypasses Python GIL | DE, MLE, DS, BE |
| Multithreading *(coming soon)* | I/O-bound parallelism | DE, BE |
| concurrent.futures *(coming soon)* | Unified threading + multiprocessing API | DE, BE |
| Dask *(coming soon)* | Distributed DataFrames, larger-than-RAM data | DE, DS |
| Ray *(coming soon)* | Distributed computing across clusters | MLE, DE |
| Polars Lazy Evaluation *(coming soon)* | Fast parallelized DataFrames | DE, DS |

### Databases *(coming soon)*
### ML Systems *(coming soon)*
### Data Processing *(coming soon)*

---

## Concept Structure

Every concept folder contains:
```
concept-name/
├── README.md   ← explanation, why, where, roles, output
└── demo.py     ← runnable code with comments
```

---

## Legend

| Role | Meaning |
|---|---|
| DE | Data Engineer |
| MLE | ML Engineer |
| DS | Data Scientist |
| BE | Backend Engineer |
