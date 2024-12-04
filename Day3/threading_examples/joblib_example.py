from math import sqrt
from functools import wraps
from time import time
import math

from joblib import Parallel, delayed # pip install joblib

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result
    return wrap


@timing
def single_thread():
    calculating = [sqrt(i ** 2) for i in range(10**7 * 2)]
    return calculating


@timing
def multithreading():
    calculating_parallel = Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10**7))
    return calculating_parallel

# Helper function to calculate square root for a range of values
def calculate_range(start, end):
    return [sqrt(i ** 2) for i in range(start, end)]

@timing
def multiprocessing_example():
    n_jobs = 12  # nie wpisywac -1!!! spojrz na linijke chunk_size i co sie wtedy stanie
    n = 10 ** 7 * 2
    chunk_size = n // n_jobs  # prace trzeba podzielic

    results = Parallel(n_jobs=n_jobs)(
        delayed(calculate_range)(i, i + chunk_size) for i in range(0, n, chunk_size)
    )
    # flatten results
    return [item for sublist in results for item in sublist]

if __name__ == '__main__':
    single_thread()
    multiprocessing_example()


# def calculate_sum(data: list[int], start: int, end: int, result: list[int]):
#     partial_sum = sum(data[start:end])
#     result.append(partial_sum)
#
#
# def main_threading():
#     data = list(range(1000000))
#     num_threads = 4
#     chunk_size = len(data) // num_threads
#
#     result = []
#     threads = []
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = start + chunk_size if i < num_threads - 1 else len(data)
#         thread = threading.Thread(target=calculate_sum, args=(data, start, end, result))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#     total_sum = sum(result)
#     print("Total sum:", total_sum)


    def calculate_sum(data_chunk: list[int]) -> int:
        return sum(data_chunk)

    data = list(range(1000000))
    num_threads = 4
    chunk_size = len(data) // num_threads

    chunks = [data[i * chunk_size: (i+1) * chunk_size] for i in range(num_threads)]
    results = Parallel(n_jobs=num_threads)(delayed(calculate_sum)(chunk) for chunk in chunks)

    total_sum = sum(results)
    print(total_sum)


    def is_prime(num:int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = int(math.sqrt(num)) + 1
        for divisor in range(3, sqrt_num, 2):
            if num % divisor == 0:
                return False
        return True


### Zadanie Napisz funkcję, która przyjmuje zakres liczb całkowitych i używa joblib do równoległego wyszukiwania liczb pierwszych w tym zakresie.

    def find_primes_in_range(start: int, end: int):
        start_time = time()

        # tutaj uzupelnic  primes =
        primes =

        end_time = time()
        prime_numbers = [num for num, is_prime in zip(range(start, end + 1), primes) if is_prime]
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        return prime_numbers


    primes = find_primes_in_range(1,10000)
    for prime in primes:
        print(prime)

























 # ROZWIAZANIE


 # tutaj uzupelnic  primes = Parallel(n_jobs=-1)(delayed(is_prime)(num) for num in range(start, end + 1))