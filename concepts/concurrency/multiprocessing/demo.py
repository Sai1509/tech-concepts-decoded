"""
Multiprocessing Demo
====================
Demonstrates the real performance difference between sequential
and parallel execution for CPU-bound tasks.

Run with:
    python demo.py
"""

import multiprocessing
import time
import os


def cpu_heavy_task(task_id):
    """Simulates a CPU-bound task that takes ~2 seconds."""
    start = time.time()
    deadline = time.time() + 2.0
    while time.time() < deadline:
        pass
    elapsed = time.time() - start
    print(f"  Task {task_id} done in {elapsed:.2f}s  (worker pid: {os.getpid()})")
    return task_id


def process_chunk(chunk_id):
    """Simulates processing one chunk of a large dataset."""
    rows_per_chunk = 10_000
    data = list(range(rows_per_chunk))
    result = sum(x * x for x in data)
    print(f"  Chunk {chunk_id}: {rows_per_chunk} rows processed")
    return rows_per_chunk


def main():
    num_tasks = 4
    task_ids = list(range(1, num_tasks + 1))

    print("=" * 60)
    print(" MULTIPROCESSING DEMO")
    print("=" * 60)

    # 1. Sequential
    print("\n[1] SEQUENTIAL EXECUTION")
    print("-" * 60)
    print(f"Running {num_tasks} tasks one after another...")
    start = time.time()
    for task_id in task_ids:
        cpu_heavy_task(task_id)
    sequential_time = time.time() - start
    print(f"Total sequential time: {sequential_time:.2f}s")

    # 2. Multiprocessing
    print("\n[2] MULTIPROCESSING EXECUTION")
    print("-" * 60)
    print(f"Running {num_tasks} tasks in parallel...")
    start = time.time()
    with multiprocessing.Pool(processes=num_tasks) as pool:
        pool.map(cpu_heavy_task, task_ids)
    parallel_time = time.time() - start
    print(f"Total multiprocessing time: {parallel_time:.2f}s")
    print(f"\nSpeedup: {sequential_time / parallel_time:.2f}x faster")

    # 3. Pool.map() real-world pattern
    print("\n[3] POOL.MAP() — THE REAL-WORLD PATTERN")
    print("-" * 60)
    num_chunks = 8
    print(f"Processing a dataset of {num_chunks} chunks in parallel...")
    start = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(process_chunk, list(range(num_chunks)))
    chunk_time = time.time() - start
    print(f"All chunks done in {chunk_time:.2f}s")
    print(f"Total rows processed: {sum(results):,}")


if __name__ == "__main__":
    main()
