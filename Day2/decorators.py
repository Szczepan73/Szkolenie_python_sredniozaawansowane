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


    @sleeper(sleep_time=2.5)                          #  dekorator =  sleeper(sleep_time=2.5)
                                                      #  slow_add = dekortor( slow_add )
    def slow_add(a: float, b: float) -> float:
        return a + b

    print(f'Wynik dodawania 2+2=')
    print(f'{slow_add(2, 2)}')


    # Stwórz dekorator, który sprawdza, czy użytkownik ma odpowiednie uprawnienia do wywołania funkcji. Jeśli nie, wyświetli komunikat o braku dostępu.






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