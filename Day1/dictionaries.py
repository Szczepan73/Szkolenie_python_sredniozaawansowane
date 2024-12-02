import operator
import random
import os
import re
from audioop import reverse
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

    najgorszy_student_2 = min(studenci,
                            key=lambda klucz: studenci[klucz]['srednia_ocen'])

    print(najgorszy_student)
    studenci.pop(najgorszy_student[0])
    print("Studenci po usunięciu najgorszego:", studenci)

    employees = [
        {"name": "John", "salary": 50000},
        {"name": "Jane", "salary": 55000},
        {"name": "Jim", "salary": 60000}
    ]

    # uzupelnij
    highest_salary_employee = max(employees, key=lambda element_listy: element_listy['salary'])
    print(highest_salary_employee)


    # Posortuj studentów według nazwiska - sorted
    studenci_posortowani = dict(   sorted(studenci.items(), key=lambda item: item[1]['nazwisko'], reverse=True)  )

    for key in studenci_posortowani:
        print(f'{key}: {studenci_posortowani[key]}')

    ############### Sets - zbiory / zestawy
    list1 = [1, 2, 3, 4, 5, 5]
    list2 = [4, 5, 6, 7, 8]

    # Convert lists into sets
    set1 = set(list1)
    set2 = set(list2)

    print(list1)
    print(set1)

    # Perform set operations
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set1 = set1.difference(set2)
    difference_set2 = set2.difference(set1)
    symmetric_difference_set = set1.symmetric_difference(set2)

    # Display the results
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference of Set 1 - Set 2:", difference_set1)
    print("Difference of Set 2 - Set 1:", difference_set2)
    print("Symmetric Difference:", symmetric_difference_set)




    # https://www.pythonmorsels.com/time-complexities/
    # https://realpython.com/python-data-structures/





    nazwa_pliku = 'text.txt'
    wystapienia = {}
    # Defining the dict
    wystapienia2 = defaultdict(int)  # from collections import defaultdict

    with open(nazwa_pliku, "r", encoding='utf-8') as plik:
        for linia in plik:
            linia_wyczyszczona = re.sub(r'\W+', ' ', linia)
            slowa = linia_wyczyszczona.lower().split()
            for slowo in slowa:
                wystapienia2[slowo] += 1
                # if slowo in wystapienia:  # https://www.geeksforgeeks.org/defaultdict-in-python/
                #     wystapienia[slowo] += 1
                # else:
                #     wystapienia[slowo] = 1

    print(wystapienia2)

    posortowane_wystapienia = dict(sorted(wystapienia2.items(), key=lambda x: x[1], reverse=True))
    print(posortowane_wystapienia)



    # Masz listę zawierającą informacje o pracownikach w firmie. Każdy pracownik jest reprezentowany przez słownik zawierający jego imię, wiek, dział i wynagrodzenie. Twoim zadaniem jest przeanalizowanie tych danych i wykonanie kilku operacji na tej liście.
    #
    # pracownicy = [
    #     {'imie': 'Jan', 'wiek': 28, 'dzial': 'IT', 'wynagrodzenie': 7000},
    #     {'imie': 'Anna', 'wiek': 34, 'dzial': 'HR', 'wynagrodzenie': 5000},
    #     {'imie': 'Marek', 'wiek': 45, 'dzial': 'IT', 'wynagrodzenie': 8000},
    #     {'imie': 'Zofia', 'wiek': 29, 'dzial': 'Marketing', 'wynagrodzenie': 6000},
    #     {'imie': 'Krzysztof', 'wiek': 31, 'dzial': 'IT', 'wynagrodzenie': 7200},
    #     {'imie': 'Agnieszka', 'wiek': 26, 'dzial': 'HR', 'wynagrodzenie': 4800},
    #     {'imie': 'Paweł', 'wiek': 38, 'dzial': 'Marketing', 'wynagrodzenie': 6500}
    # ]
    #
    #
    # 1. Utwórz listę zawierającą imiona wszystkich pracowników
    # 2. Oblicz średnie wynagrodzenie pracowników
    # 3. Znajdź pracowników z działu 'IT' i utwórz ich osobną listę
    # 4. Posortuj listę pracowników według wieku rosnąco
    # 5. Odwróć listę pracowników
    # 6. Sprawdź, czy istnieje pracownik o imieniu 'Anna' na liście
    # 7. Dodaj nowego pracownika do listy
    # 8. Usuń pracownika z najniższym wynagrodzeniem z listy
    # 9. Zaktualizuj wynagrodzenie wszystkich pracowników z działu 'HR', podnosząc je o 10%
    # 10. Wyczyść listę pracowników

