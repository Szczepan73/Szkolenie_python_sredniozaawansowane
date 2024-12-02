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