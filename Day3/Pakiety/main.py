import os
import sys

import pandas as pd


# # Importowanie całego modułu lub pakietu:
# import my_package.module1
# my_package.module1.function1()
#
#
# # Importowanie konkretnej funkcji lub klasy:
# from my_package.module1 import function1
# function1()
#
# #Importowanie z aliasem (krótsza nazwa):
# import my_package.module1 as m1
# m1.function1()
#
# #Importowanie wszystkich elementów modułu (niezalecane):
# from my_package.module1 import *
#
# # Jeśli używasz from module import *, tylko te nazwy, które są wymienione w __all__, zostaną zaimportowane.
# # Jeśli __all__ nie istnieje, zaimportowane zostaną wszystkie nazwy, które nie zaczynają się od podkreślenia "_"



# from PodPakiet import functions
from PodPakiet.functions import times3


# from Day2.classes_and_objects import Zawodnik # uwaga wykonuje sie cały kod z tego skryptu




# Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było podawać nazwy pakietu ani modułu.
# W tym module dopisz funkcje walidacji danych dla funkcji BMI - czy waga < 200 i 1.00 < wzrost < 2.50. Jesli warunek nie jest spelniony
# rzuc wyjatkiem Value error. # raise ValueError("wiadomosc bledu")
# W pliku __init__.py ustaw zmienna __all__ tak aby tylko funkcja liczac BMI byla widoczna po imporcie pakietu
# dodajcie print do pliku __init__.py


from BodyMassIndex import calculate_bmi




if __name__ == "__main__":
    df = pd.DataFrame()

    # print(functions.times3(3))
    print(times3(3))

    # print(_times4(4))

    try:
        height = [2.11, 1.80]
        weight = [100, 400, 120]
        for h, w in zip(height, weight):
            bmi_result = calculate_bmi(h, w)
            print("Your BMI is:", bmi_result)
    except ValueError as e:
        print("Error:", e)

    # dokumentacja i sprawdzanie infomracji
    help(calculate_bmi)

    import BodyMassIndex
    # Wywołanie docstringa pakietu
    print(BodyMassIndex.__doc__)

    # Sprawdzanie wersji pakietu
    print("Package version:", BodyMassIndex.__version__)  # scipy==1.0

    # print(os.getenv("PYTHONPATH")) # tylko w trybie DEBUG pycharm ustawia tą zmienną,
    # ale możemy ją też mieć ustawioną globalnie w systemie, jeśli korzystamy z venv, conda lub innych srodowisk wirtualnych to nie ustawiamy tej zmiennej

    # PYTHONPATH to zmienna środowiskowa, która określa dodatkowe ścieżki, w których Python szuka modułów i pakietów podczas importowania.
    # Jest ona szczególnie przydatna, gdy trzeba zaimportować moduły lub pakiety, które nie znajdują się w standardowych lokalizacjach.
    print("\n".join(sys.path))





    # Problemy i pułapki
    # 1. Cykliczne importy

    # module1.py
    # from my_package.module2 import func2

    # module2.py
    # from my_package.module1 import func1

    # 2. Błędy w importach względnych

    # from .module import foo  # Działa tylko w pakiecie, nie jako skrypt uruchamiany wprost
    # Rozwiązanie: Użyj importu absolutnego (import package.module)

    # 3. Konflikty nazw modułów
    # Jeśli nazwiesz swój plik `random.py`:
    # import random  # Może zaimportować twój plik zamiast modułu standardowego
