import threading
import multiprocessing
import asyncio
import time


# ---------------------------------
# I/O-BOUND TASK
# ---------------------------------

def io_task(task_number):
    print(f"I/O Task {task_number} started")
    time.sleep(1)
    print(f"I/O Task {task_number} completed")


# ---------------------------------
# THREADING
# ---------------------------------

def run_threading():
    print("\n--- THREADING ---")

    start = time.perf_counter()

    threads = []

    for i in range(5):
        thread = threading.Thread(target=io_task, args=(i + 1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter()

    print(f"Threading Time: {end - start:.2f} seconds")


# ---------------------------------
# ASYNCIO
# ---------------------------------

async def async_task(task_number):
    print(f"Async Task {task_number} started")
    await asyncio.sleep(1)
    print(f"Async Task {task_number} completed")


async def run_asyncio():
    print("\n--- ASYNCIO ---")

    start = time.perf_counter()

    tasks = []

    for i in range(5):
        tasks.append(async_task(i + 1))

    await asyncio.gather(*tasks)

    end = time.perf_counter()

    print(f"AsyncIO Time: {end - start:.2f} seconds")


# ---------------------------------
# CPU-BOUND TASK
# ---------------------------------

def cpu_task(number):
    total = 0

    for i in range(1, 5_000_000):
        total += i * number

    return total


# ---------------------------------
# MULTIPROCESSING
# ---------------------------------

def run_multiprocessing():
    print("\n--- MULTIPROCESSING ---")

    start = time.perf_counter()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_task, [1, 2, 3, 4])

    end = time.perf_counter()

    print("CPU tasks completed")
    print(f"Multiprocessing Time: {end - start:.2f} seconds")


# ---------------------------------
# MAIN PROGRAM
# ---------------------------------

if __name__ == "__main__":

    print("======================================")
    print("THREADING vs MULTIPROCESSING vs ASYNCIO")
    print("======================================")

    run_threading()

    asyncio.run(run_asyncio())

    run_multiprocessing()

    print("\n======================================")
    print("All tasks completed")
    print("======================================")