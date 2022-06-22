"""
Process is an instance of a program
- Takes advantage of multiple CPUs and cores
- Seperate memory space -> Memory is not shared between processes
- Greate for CPU-bound processing
- New process is stated independently from another processes
- Processes are interruptable/killable
- One GIL for each process -> avoids GIL Limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More Memory 
- IPC is more complicated




Thread is an entity within a process that can be scheduled
A process can spawn multiple threads


- All thread within a process share the same memory
- Starting a thread is faster than starting a process
- Great for I/O tasks
- Threading is limited by GIL
- No effect for CPU-bound tasks
- Not interruptable/killable
-careful with race conditions






GIL 
Globl Interpreter Lock
Only One thread at a time to execute
Needed in CPython because memory management is not thread safe
"""


from multiprocessing import Process
import time
import os

processes = []
num_processes = os.cpu_count()


print(num_processes)


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)


for p in processes:
    p.start()


for p in processes:
    p.join()


print("end main")
