import time
import threading
import concurrent.futures

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done Sleeping")


# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


threads = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    # t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()
print(f"finished in {round(finish-start,2)} seconds")


##################################################################################
# Thread Pool Executor


def do_something(sec):
    print("Sleeping 1 second")
    time.sleep(sec)
    return "Done Sleeping"


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something,1)
#     f2 = executor.submit(do_something,1)
#     print(f1.result())
#     print(f2.result())

start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    results = executor.map(do_something,secs)
    # for result in results:
    #     print(result)
finish = time.perf_counter()
print(f"finished second round in {round(finish-start,2)} seconds")