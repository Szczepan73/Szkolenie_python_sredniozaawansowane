import operator
import random
import os
import re
from collections import defaultdict


if __name__ == '__main__':
    slownik = {}
    slownik2 = dict()

    info = {
        "LG123": "Telewizor 60' z HD Ready, wejściem na internety ifiltrem reklam",
        "SONY666": "Piekielnie dobry telewizor",
        "SZAJSUNG999": "Telewizor świetnie nadający się do zakrycia dziury w ścianie(i niczego więcej)"
    }

    print(info)
    print(info["LG123"])
    print(info.keys())
    print(info.values())

    print(info.get("Niematakiego", "WartoscZwracana"))

    # print(info["abc"])

    info["abc"] = "Jakis teskt"
    print(info["abc"])

    info["SZAJSUNG999"] = "Brak informacji"
    print(info["SZAJSUNG999"])

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')

    for key in info.keys():
        print(info[key])

    if "LG123" in info:
        print("Mamy LG")
    else:
        print("niet :(")

    people = {}

    with open("dane.txt", "r") as file:
        for line in file:
            line_splited = line.rstrip().split(';')

            if len(line_splited) == 3:
                people[line_splited[0]] = (line_splited[1], line_splited[2])
            else:
                print(f"Blad w lini {line_splited}")

    for key, value in people.items():
        print(f"Key: {key}: value: {value}")

    # wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
    # druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
    ustawienia = {}

    with open("ustawienia.txt", "r") as file:
        for line in file:
            line = line.strip().split(';')
            if len(line) == 2:
                key, value = line
                ustawienia[key] = value

    for key, value in ustawienia.items():
        print(f'Klucz: {key}, wartosc: {value}')


    ###########################################


    studenci = {
        1001: {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 21, 'oceny': [4, 3, 5, 4]},
        1002: {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [5, 5, 4, 5]},
        1003: {'imie': 'Marek', 'nazwisko': 'Zielinski', 'wiek': 23, 'oceny': [3, 4, 2, 3]},
        1004: {'imie': 'Zofia', 'nazwisko': 'Wiśniewska', 'wiek': 20, 'oceny': [4, 4, 4, 4]},
        1005: {'imie': 'Krzysztof', 'nazwisko': 'Wojcik', 'wiek': 24, 'oceny': [2, 3, 2, 3]}
    }

    studenci[1006] = {'imie': 'Krzysztof2', 'nazwisko': 'Wojcik', 'wiek': 26, 'oceny': [4, 3, 3, 3, 4, 5]}


    list_of_names = [studenci[id]['imie'] for id in studenci]
    print(list_of_names)


    # imie studenta i jego najwysza ocena
    for id_studenta in studenci:
        oceny = studenci[id_studenta]['oceny']
        najwysza_ocena = max(oceny)
        print(f"{studenci[id_studenta]['imie']}  - max ocena {najwysza_ocena}")


    #  Oblicz średnią ocenę dla każdego studenta i dodaj ją do ich słownika
    # studenci[id_studenta]['srednia_ocen'] = 4.5

    for id_studenta in studenci:
        oceny = studenci[id_studenta]['oceny']
        srednia = sum(oceny) / len(oceny)
        studenci[id_studenta]['srednia_ocen'] = srednia

    print(studenci)

    ###############

    nazwiska = ['Kowalski', 'Nowak', 'Zielinski', 'Wiśniewska', 'Wojcik']
    dlugosci_nazwisk = {nazwisko: len(nazwisko) for nazwisko in nazwiska if len(nazwisko) > 6}
    print(dlugosci_nazwisk)

    #  Znajdź studentów, którzy mają średnią ocenę powyżej 4.0, stworz słownik id: słownik
    # studenci.items()  ---> klucz i wartosc    wartosc['kluczem']
    studenci_pow_4 = {id_studenta: dane for id_studenta, dane in studenci.items() if dane['srednia_ocen'] > 4.0}
    print(studenci_pow_4)


    ######################################################


    # lambda argumenty : wyrażenie
    p = lambda argumenty: print(argumenty)
    p("moj napis")

    # Tak nie robić !!! to juz za duzo na lambde
    calculate = lambda x, y: x + y if x > y else x - y
    print(calculate(5, 10))


    # lepiej tak
    def calculate(x, y):
        if x > y:
            return x + y
        else:
            return x - y


    liczby = [1, 2, 3, 4, 5]
    powers = list(map(lambda x: x ** 2, liczby))    # for element in list: wywolja_funkcje(element)
    print(powers)

    #########
    najgorszy_student = min(studenci.items(), key=lambda klucz_i_wartosc: klucz_i_wartosc[1]['srednia_ocen'])   # (klucz, wartosci)
    print(najgorszy_student)
    studenci.pop(najgorszy_student[0])
    print("Studenci po usunięciu najgorszego:", studenci)

    employees = [
        {"name": "John", "salary": 50000},
        {"name": "Jane", "salary": 55000},
        {"name": "Jim", "salary": 60000}
    ]

    # uzupelnij
    highest_salary_employee = max(employees, key=)
    print(highest_salary_employee)