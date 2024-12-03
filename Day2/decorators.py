import operator
import random
import os
import re

from datetime import datetime
import time
import functools
from typing import Callable
import statistics

if __name__ == '__main__':
    # https://refactoring.guru/pl/design-patterns/decorator
    print("Hello day 2")


    def dekorator_z_1_parametrem(fun):
        def wew(liczba: int):
            print("Hurra działa z parametrem")
            print(fun(liczba))

        return wew


    @dekorator_z_1_parametrem
    def dodaj_cztery(liczba: int) -> int:
        return liczba + 4

    dodaj_cztery(4)


    def dekorator_do_funkcji_z_parameterami(fun):
        def wew(*args, **kwargs):
            print("Hurra działa zawsze")
            fun(*args, **kwargs)
            print("Po wszystkim")

        return wew


    @dekorator_do_funkcji_z_parameterami
    def dekorowana(x: str):
        print(f'siema {x}')


    @dekorator_do_funkcji_z_parameterami
    def dekorowana_bez_p():
        print(f'siema')


    dekorowana("Janek")
    dekorowana(x="Wojtek")
    dekorowana_bez_p()


    @dekorator_do_funkcji_z_parameterami
    def moja_suma(*liczby: tuple[int, ...]) -> int:
        suma = 0
        for i in liczby:
            suma += i
        return suma


    moja_suma(1, 2, 3, 3, 4, 5)


    # Napisz funkcje która przed i po wykonaniu innej funkcji wypisze 25 '*'     print("*" * 25)
    def star(func):
        def inner(*args, **kwargs):
            print("*" * 25)
            func(*args, **kwargs)
            print("*" * 25)

        return inner


    def percent(func):
        def inner(*args, **kwargs):
            print("%" * 15)
            func(*args, **kwargs)
            print("%" * 15)

        return inner


    @percent
    @star
    def printer(msg: str):   # printer = percent(star(printer))
        print(msg)


    printer("Hello World")


    @star
    def printer_2(msg: str, count: int):
        print(msg * count)

    printer_2("Hello World", 2)


    def hello_decorator(func):
        def inner1(*args, **kwargs):
            print("before Execution")

            # getting the returned value
            returned_value = func(*args, **kwargs)
            print("after Execution")

            # returning the value to the original frame
            return returned_value

        return inner1


    @hello_decorator
    def sum_two_numbers(a: int, b: int) -> int:          # sum_two_numbers = hello_decorator(sum_two_numbers)
        print("Inside the function sum_two_numbers")
        return a + b


    result = sum_two_numbers(12, 4)
    print(f"Wynik dodawania: 12 + 4 = {result}")


    # Dodaj dekorator który zliczy czas wykonywania tej funkcji z parametrami. Zaloguj na konsole wszystkie przekazane parametry
    def licz_czas_i_loguj(fun):
        @functools.wraps(fun)
        def wewnetrzna(*args, **kwargs):
            print(f'Argumenty {args}')
            print(f'Key-word arguments {kwargs}')
            poczatek = datetime.now()
            value = fun(*args, **kwargs)
            koniec = datetime.now()
            print(f'wywolanie trwalo {koniec - poczatek}')
            return value

        return wewnetrzna


    @licz_czas_i_loguj
    def opakuj_mnie_z_parametrami(x, napis_do_wypisania):    # opakuj_mnie_z_parametrami = licz_czas_i_loguj(opakuj_mnie_z_parametrami)
        """
        Ta funkcja spi przez x sekund a nastpenie wypisuje wiadomosc

        Parameters
        ----------
        x : int powinien miec wartosc wieksza od 0
        napis_do_wypisania

        Returns
        -------
        Zawsze zwraca 10
        """
        for i in range(x):
            time.sleep(0.1)
        print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")
        return 10


    returned_value = opakuj_mnie_z_parametrami(x=1, napis_do_wypisania="jestem cool")
    print(returned_value)

    # print(opakuj_mnie_z_parametrami.__doc__)
    help(opakuj_mnie_z_parametrami)
    print(opakuj_mnie_z_parametrami.__name__)


    def sleeper(sleep_time:float):
        def sleeper_decorator(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                time.sleep(sleep_time)    # sleep_time = 2.5
                returned_value = func(*args, **kwargs)
                return returned_value

            return inner

        return sleeper_decorator


    @sleeper(sleep_time=0.1)                          #  dekorator =  sleeper(sleep_time=2.5)
                                                      #  slow_add = dekortor( slow_add )
    def slow_add(a: float, b: float) -> float:
        return a + b

    print(f'Wynik dodawania 2+2=')
    print(f'{slow_add(2, 2)}')


    # Stwórz dekorator, który sprawdza, czy użytkownik ma odpowiednie uprawnienia do wywołania funkcji. Jeśli nie, wyświetli komunikat o braku dostępu.
    def check_permissions(required_permission: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(user: dict[str,str], *args, **kwargs):
                if user.get('permission') == required_permission:
                    return func(user, *args, **kwargs)
                else:
                    print("Brak uprawnień do wykonania tej funkcji")

            return wrapper

        return decorator



    @check_permissions('user')
    def user_function(user):
        print(f"Witaj, użytkowniku {user['name']}")


    @check_permissions('admin')
    def admin_function(user):
        print("Witaj, adminie!")

    user1 = {'name': 'Jan', 'permission': 'admin'}
    user2 = {'name': 'Anna', 'permission': 'user'}

    admin_function(user1)  # Output: Witaj, adminie!
    admin_function(user2)  # Output: Brak uprawnień do wykonania tej funkcji
    user_function(user2)  # Output: Witaj, użytkowniku!
    user_function(user1)  # Output: Brak uprawnień do wykonania tej funkcji


    def timeit(repeats: int = 10):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                times = []
                for _ in range(repeats):
                    start_time = time.time()
                    result = func(*args, **kwargs)
                    end_time = time.time()
                    times.append(end_time - start_time)

                avg_time = statistics.mean(times)
                std_dev = statistics.stdev(times) if len(times) > 1 else 0.0

                print(f"Function '{func.__name__}' executed {repeats} times.")
                print(f"Average execution time: {avg_time:.6f} seconds")
                print(f"Standard deviation: {std_dev:.6f} seconds")

                return result

            return wrapper

        return decorator


    @timeit(repeats=50)
    def slow_function(seconds):
        print(f"Sleeping for {seconds} seconds...")
        time.sleep(seconds)
        return f"Slept for {seconds} seconds"


    # print(slow_function(0.1))



    def cache(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = args + tuple(kwargs.values())
            if cache_key not in wrapper.cache_dict:
                wrapper.cache_dict[cache_key] = func(*args, **kwargs)
                return wrapper.cache_dict[cache_key]
            else:
                print("Using cached value")
                return wrapper.cache_dict[cache_key]

        wrapper.cache_dict = {}
        return wrapper


    @cache
    def mnozenie(a: float, b: float) -> float:
        print(f'Wynik: {a * b}')
        return a * b


    mnozenie(2, 2)
    mnozenie(2, 2)

    mnozenie(2, 3)
    mnozenie(3, 2)

    mnozenie(b=3, a=2)

    print(mnozenie.cache_dict)



    # https://realpython.com/primer-on-python-decorators/#more-real-world-examples
    # https://refactoring.guru/pl/design-patterns/catalog
    # https://github.com/lord63/awesome-python-decorator