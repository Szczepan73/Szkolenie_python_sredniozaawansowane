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



    suma = moja_suma(1, 2, 3, 4, 5, 15, 18, 50)
    suma2 = moja_suma(1, 2, 3, 4, 5, 15, 18, 50,10,4,3,4,5,6,7,8,9)
    print(suma)