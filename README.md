# Threading vs Multiprocessing vs AsyncIO
📌 Project Overview
This project compares three Python concurrency approaches:
•🧵 Threading
•⚡ AsyncIO
•🔥 Multiprocessing

The project runs suitable workloads and measures their execution time to understand when each approach should be used.

🎯 Objective:
To understand the differences between Threading, Multiprocessing, and AsyncIO and learn which approach is suitable for I/O-bound and CPU-bound tasks.

🛠️ Technologies Used:
•Python
•threading
•multiprocessing
•asyncio
•time

📂 Project Structure:
concurrency_comparison/
│
└── main.py

📊 Example Output:
======================================
THREADING vs MULTIPROCESSING vs ASYNCIO
======================================

--- THREADING ---
I/O Task 1 started
I/O Task 2 started
I/O Task 3 started
I/O Task 4 started
I/O Task 5 started
Threading Time: 1.01 seconds

--- ASYNCIO ---
Async Task 1 started
Async Task 2 started
Async Task 3 started
Async Task 4 started
Async Task 5 started
AsyncIO Time: 1.00 seconds

--- MULTIPROCESSING ---
CPU tasks completed
Multiprocessing Time: 1.20 seconds

======================================
All tasks completed
======================================
