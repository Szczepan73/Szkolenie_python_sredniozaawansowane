import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
from typing import Callable, Tuple, List, Union


def times2(a: int | list[int]) -> str | int:  # Union[str, int]
    if a == 0:
        return "przez zero nie mnoze"
    return a * 2


if __name__ == '__main__':
    print(times2(2))

    print(times2("string"))

    print(type(times2([1, 2, 3, 4])))
    print(times2([1, 2, 3, 4]))


    def funckja_jako_argument(f: Callable, x: int):
        print(f(x))


    funckja_jako_argument(times2, 32)
    funckja_jako_argument(lambda arg: arg + 2, 3)


    def powieksz(x: str) -> str:
        return x.upper()

    def tytul(napis: str) -> str:
        return napis.title()


    def zastosuj_dla_wszystkich(fun: Callable, *strings):    # *args
        print(strings)
        print(type(strings))
        for a in strings:
            print(fun(a))


    zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak', 'aaaaa')
    zastosuj_dla_wszystkich(tytul, 'siała', 'baba', 'mak', )


    # Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
    def moja_suma(*liczby: tuple[int, ...]) -> int:
        suma = 0
        for i in liczby:
            suma += i
        return suma


    # def moja_suma(*liczby: tuple[int, ...]) -> int:
    #    return sum(liczby)

    suma = moja_suma(1, 2, 3, 4, 5, 15, 18, 50)
    suma2 = moja_suma(1, 2, 3, 4, 5, 15, 18, 50,10,4,3,4,5,6,7,8,9)
    print(suma)

    #################################

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]

    print(moja_suma(*list1, *list2, *list3))  # *list1 = 1,2,3

    def my_sum(a, b, c):
        print(f"a={a}")
        print(a + b + c)


    slownik = {"c": 2, "a": 4, "b": 3}
    my_sum(**slownik)   # my_sum(a=4,b=3,c=2)
    my_sum(*list1)  #my_sum(1,2,3)


    def pomnoz_razy_dwa(x):
        return x * 2

    def podziel_przez_trzy(x):
        return x / 3

    def dodaj_piec(x):
        return x + 5


    funkcje = [pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec]

    def aplikuj(wartosc: int, *funckje) -> float:
        for f in funckje:
            wartosc = f(wartosc)
        return wartosc


    print(aplikuj(1, *funkcje))
    print(aplikuj(1, pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec, times2))


    def wiele_argumentów(*args):
        ile_ich = len(args)
        print(ile_ich)
        for element in args:
            print(element, type(element))


    wiele_argumentów([1], "abc", 1.0, 123, "Moj super kurs pythona")


    # Napisz funkcję process_data, która:
    #
    # Przyjmuje dowolną liczbę argumentów pozycyjnych (*args), które mogą być liczbami, stringami lub listami.
    # Jeśli argument jest liczbą, dodaje ją do wyniku.
    # Jeśli argument jest stringiem, konkatenuje go do wyniku.
    # Jeśli argument jest listą, sumuje wszystkie jej elementy.

    def process_data(*args):
        total_sum = 0
        concatenated_string = ""
        list_sum = 0

        for item in args:
            if isinstance(item, int) or isinstance(item, float):
                total_sum += item
            elif isinstance(item, str):
                concatenated_string += item
            elif isinstance(item, list):
                list_sum += sum(item)

        return total_sum, concatenated_string, list_sum


    # Test
    result = process_data(1, "Hello", [1, 2], 3, "World", [3, 4])
    print(result)  # Wyjście: (4, "HelloWorld", 10)

    ##############################################


    def funkcja_przykladowa(arg1, *args, **kwargs):
        print("arg1:", arg1)
        print("args:", args)
        print("kwargs:", kwargs)


    funkcja_przykladowa(1, 2, 3, 4, imie='Anna', wiek=30)


    def parametr_kwargs(**kwargs):
        for k in kwargs:
            print(k, kwargs[k])


    parametr_kwargs(dodatkowy=48, nastepny=111)


    def zapisz_parametry_do_pliku(nazwa_pliku, **parametry):
        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in parametry:
            plik.write(f'{p};{parametry[p]}\n')
        plik.close()


    studenci = {
        "1001": {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 21, 'oceny': [4, 3, 5, 4]},
        "1002": {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [5, 5, 4, 5]},
        "1003": {'imie': 'Marek', 'nazwisko': 'Zielinski', 'wiek': 23, 'oceny': [3, 4, 2, 3]},
        "1004": {'imie': 'Zofia', 'nazwisko': 'Wiśniewska', 'wiek': 20, 'oceny': [4, 4, 4, 4]},
        "1005": {'imie': 'Krzysztof', 'nazwisko': 'Wojcik', 'wiek': 24, 'oceny': [2, 3, 2, 3]}
    }

    zapisz_parametry_do_pliku('mojplik.csv', parametr1='wartość 1', parametr2=2,
                              moj_argument="Jestesmy zmeczeni bardzo", **studenci)

    parametry = {"param1": 1, "param2": 2, "param3": 3}

    zapisz_parametry_do_pliku('mojplik2.csv', **parametry)


    # Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
    # Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego pierwsza jest nazwa
    # argumentu a druga jego wartoscia. Jesli dane argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac
    # jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.





    config("plik.csv", wersja=1, arg=2, argument321=3, parametr1="wartość 2")
    config("plik.csv", arg_inny=2, argument321=10, wersja=2.0)
