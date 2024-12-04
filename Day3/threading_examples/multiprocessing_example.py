import multiprocessing
import time

def cpu_bound_task():
    # Intensywnie obliczeniowa operacja
    count = 0
    for _ in range(10**7):
        count += 1

if __name__ == "__main__":
    start_time = time.time()

    # Uruchamiamy dwa procesy, każdy wykonujący cpu_bound_task
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=cpu_bound_task)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Time taken: {time.time() - start_time:.2f} seconds")