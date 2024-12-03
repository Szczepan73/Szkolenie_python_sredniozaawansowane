from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd
from functools import total_ordering   # fills in missing comparison methods (<, <=, >, >=) based on just two: either __eq__ and one other comparison method like __lt__ or __gt__.


class Osoba(object):

    def __init__(self, imie: str, nazwisko:str, wiek: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print(self.imie, self.nazwisko, self.wiek)

    def __str__(self):
        return f'Cześć jestem: {self.imie}, {self.nazwisko}, {self.wiek}'

    def __repr__(self):
        return f"Osoba({self.imie, self.nazwisko, self.wiek})"


o = Osoba("Wojtek", "Dudzik", 31)
o2 = Osoba("Jan", "Nowak", 25)

print(o.imie)
o.wiek += 1
print(o.wiek)

o.wypiszMnie()

o3 = Osoba(imie="Krzysztof", nazwisko="Nowak", wiek=32)

lista_osob = [o, o2, o3]

for osoba in lista_osob:
    osoba.wypiszMnie()

print(o3)
napis = str(o3)
print(napis)

#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.

# dopisz metody __str__ i __repr__ do klasy samochod
class Samochod:

    def __init__(self, marka: str, model:str, rejestracja: str):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja

    def wypiszMnie(self):
        print(self.marka, self.model, self.rejestracja)

    def __repr__(self):
        return f'Samochod("{self.marka}", "{self.model}", "{self.rejestracja}")'

    def __str__(self):
        return f'Samochod: {self.marka}, {self.model}, {self.rejestracja},'


s = Samochod("Skoda", "Octawia", 'WS124')
s2 = Samochod("Toyota", "Yaris", 'WWL642')

s.wypiszMnie()

print(f'Moj wspaniały samochód {s2}')
