import threading
import time

def cpu_bound_task():
    # Intensywnie obliczeniowa operacja
    count = 0
    for _ in range(10**7):
        count += 1

start_time = time.time()

# Uruchamiamy dwa wątki, każdy wykonujący cpu_bound_task
threads = []
for _ in range(4):
    thread = threading.Thread(target=cpu_bound_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Time taken: {time.time() - start_time:.2f} seconds")