import os

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




if __name__ == "__main__":
    df = pd.DataFrame()

    print(os.getenv("PYTHONPATH"))


    # print(functions.times3(3))
    print(times3(3))

    # print(_times4(4))



