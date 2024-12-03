from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd
from functools import total_ordering, cached_property   # fills in missing comparison methods (<, <=, >, >=) based on just two: either __eq__ and one other comparison method like __lt__ or __gt__.


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
# Wzrost jest atrybutem prywatnym (__wzrost)
# masa i imie są atrybutami chronionymi (_masa, _imie)
# stwórz właściwość Waga która będzie wykorzystywać atrybut _masa
# właściwość Waga może być zmieniana ale tyklo z wykorzystaniem dekoratora @property
# stworz właściwość BMI który będzie tylko do odczytu
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
# dodac metode __str__
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.

class Zawodnik:
    def __init__(self, wzrost: float, masa: float, imie: str):
        self.__wzrost = wzrost
        self._masa_zawodnika = masa
        self._imie = imie

    @cached_property
    def BMI(self) -> float:
        return self._masa_zawodnika / (self.__wzrost ** 2)

    @property
    def waga(self) -> float:
        return self._masa_zawodnika

    @waga.setter
    def waga(self, value: float):
        self._masa_zawodnika = value
        # self.nowe_pole = "jakas wartosc"

    def __str__(self):
        return f'Zawodnik: {self._imie}, o BMI={self.BMI:.3f}'

    @staticmethod
    def nie_uzywam_atrybutow(info: str):
        print(info)


    @classmethod
    def create_from_string(cls, text: str):
        dane = text.strip().split(';')
        if len(dane) == 3:
            wzrost_cm, waga_lbs, imie = dane
            z = cls(wzrost=int(wzrost_cm) / 100, masa=int(waga_lbs) * 0.454, imie=imie)
            return z


    # odczytali dane z pliku dane.txt
    # zbudowali sobie liste zawodnikow (jako obietky klasy) przy uzyciu  @classmethod




    # zła praktyka
    # def dodaj_atrybut_nazwisko(self, nazwisko:str):
    #     self.nazwisko = nazwisko


z = Zawodnik(1.8, 80, "Jan")

print(z)
z.waga = 75
print(z)

liczba_str = "80"
liczba_float = float(liczba_str)

z2 = Zawodnik(1.8, 80, "Karol")
print(z2)

Zawodnik.nie_uzywam_atrybutow("Hello")
z2.nie_uzywam_atrybutow("Hello world")


z3 = Zawodnik.create_from_string("176;150;Paweł")
print(z3)


list_zawodnikow = Zawodnik.create_from_file("dane.txt")
print(list_zawodnikow[0])










class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


MathUtils.add(2,2)