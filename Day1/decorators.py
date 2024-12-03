import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
from typing import Callable
import statistics


def do_opakowania():
    print("Opakuj mnie")


def dekorator(funkcje: Callable) -> Callable:
    def opakowujaca():
        print("Przed")
        funkcje()
        print("Po")

    return opakowujaca

@dekorator                  # do_opakwoanie_2 = dekorator(do_opakwoanie_2)
def do_opakwoanie_2():
    print("Skladnia dekorator pythona")


def f():
    pass

if __name__ == '__main__':
    # https://refactoring.guru/pl/design-patterns/decorator

    udekorowana = dekorator(do_opakowania)
    udekorowana()

    do_opakwoanie_2()

    # Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
    # Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()" lub datetime.now()
    def licz_czas(fun):
        def wew():
            poczatek = datetime.now()
            fun()
            koniec = datetime.now()
            print(f'Wywolanie trwalo {koniec - poczatek}')

        return wew

    @licz_czas
    def opakuj_mnie():
        #time.sleep(3)
        print("Robie ciekawe rzeczy w Pythonie")

    opakuj_mnie()


    @licz_czas
    def opakowanie_inne():
        print("inna funkcja")

    opakowanie_inne()
