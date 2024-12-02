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

