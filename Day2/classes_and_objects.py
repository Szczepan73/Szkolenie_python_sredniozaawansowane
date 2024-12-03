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

    def __init__(self, marka: str, model:str, rejestracja: str, kierowca: Osoba = Osoba("Jan", "Nowak", 35)):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja
        self._kierowca = kierowca

    def wypiszMnie(self):
        print(self.marka, self.model, self.rejestracja)

    def __repr__(self):
        return f'Samochod("{self.marka}", "{self.model}", "{self.rejestracja}")'

    def __str__(self):
        return f'Samochod: {self.marka}, {self.model}, {self.rejestracja}, {self._kierowca}'

    def _funckje_dla_mechanika(self):
        print("Naprawiam")


s = Samochod("Skoda", "Octawia", 'WS124')
s2 = Samochod("Toyota", "Yaris", 'WWL642', o3)

s.wypiszMnie()

s._funckje_dla_mechanika()

print(f'Moj wspaniały samochód {s2}')


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def _get_radius(self):
        print("Get radius")
        return self.__radius

    # def _set_radius(self, value):
    #     print("Set radius")
    #     self.__radius = value

    radius = property(fget=_get_radius,
                      # fset=_set_radius,
                      doc="Radius property of circle")


kolo = Circle(5)
print(f"Promien {kolo.radius}")
#print(kolo._Circle__radius)

try:
    kolo.radius = 30
except Exception as err:
    print(err)


class Rectangle:
    def __init__(self, a:int, b:int):
        self._a = a
        self.b = b

    @property
    def dlugosc_a(self):
        print("Get a")
        return self._a

    @dlugosc_a.setter
    def dlugosc_a(self, value):
        print("Set a")
        self._a = value


r = Rectangle(4,2)
r.b = 8
# r.dlugosc_a = 30
print(f'Rectangle {r.dlugosc_a}, {r.b}')
r.dlugosc_a = 10
print(f'Rectangle {r.dlugosc_a}, {r.b}')


# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# stworz atrybut BMI który będzie tylko do odczytu
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# Wzrost jest atrybutem prywatnym (__wzrost)
# Waga może być zmieniana ale też jako atrybut z wykorzystaniem dekoratora @property
# waga ma być atrybutem chronionym (_waga)
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
# dodac metode __str__


