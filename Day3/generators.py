import random
import time



def elements():
    yield 'element 1'
    yield 'element 2'
    yield 'element 3'
    print("hello world")
    yield 'element 4'




if __name__ == '__main__':
    generator = elements()

    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())

    for e in elements():
        print(e)

    for i in range(10000000000000000000):
        print(i)
        if i > 10:
            break

    # start = time.time()
    # range_list = [i for i in range(100000000)]
    # end = time.time()
    # print(f'Time needed: {end - start}')
    #
    # for i in range_list:
    #     print(i)
    #     if i > 10:
    #         break


    def tens():
        i = 1
        while True:
            yield i * 10
            i += 1


    generator_tens = tens()

    print(generator_tens.__next__())
    print(generator_tens.__next__())
    print(generator_tens.__next__())

    print("And now in for loop")

    for ten in generator_tens:
        print(ten)
        if ten > 100:
            break

    # Generatory mogą symulować strumienie danych, np. sensory zbierające dane.
    def data_stream():
        while True:
            yield random.randint(1, 100)
            time.sleep(0.1)


    stream = data_stream()
    for _ in range(5):
        print(next(stream))  # Symuluje odbiór danych co sekundę


    #  Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
    #  f'element o indeksie {x}'( gdzie x bedzie numerem podawanego elementu) czekajac 1 sekunde przed zwrotem kazdego elementu.
    def generator_elementow(ilosc: int):
        for i in range(ilosc):
            time.sleep(0.1)
            yield f'element o indeksie {i}'


    genrator = generator_elementow(3)
    print(next(genrator))
    next(genrator)
    print(next(genrator))



    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


    # napisz generator ktory bedzie zwracał nieskonczenie wiele liczb pierwszych
    def prime_numbers():
        num = 2
        while True:
            if is_prime(num):
                yield num
            num += 1


    generator_of_primes = prime_numbers()

    for i in range(20):
        print(next(generator_of_primes))


    potegi2 = [2 ** i for i in range(100)]

    generator_potegi = (2 ** i for i in range(1000000000000))

    print(generator_potegi)
    print(next(generator_potegi))
    print(next(generator_potegi))
    print(next(generator_potegi))




    def read_lines_in_batches(file_path: str, batch_size: int = 3) -> list[str]:
        with open(file_path) as file:
            while True:
                batch = []
                for _ in range(batch_size):
                    line = file.readline()
                    if not line:
                        break
                    batch.append(line.strip())
                if not batch:
                    break
                yield batch


    file = r'../Day1/text.txt'
    for i, batch in enumerate(read_lines_in_batches(file, batch_size=10)):
        print(f'Batch number {i}: {batch}')