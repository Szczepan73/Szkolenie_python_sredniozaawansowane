import operator
import random
import os
import re
from collections import defaultdict


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Pyton Kurs')

    # list_BAD_example = [1, 2, 3, "napis", 3.5, 'a']

    list_example = [1, 2, 3, 4, 5, 6, 7]
    list_example2 = list() # []

    print(list_example)

    list_example.append(5)

    print(list_example)
    print(list_example[0])
    print(list_example[-1])
    print(list_example[len(list_example) - 1])

    # print(list_example[len(list_example)])  # IndexError: list index out of range
    print(list_example[1:3])    # [1, 2, 3, 4, 5, 6, 7, 5]
    print(list_example[:3])
    print(list_example[2:])
    print(list_example[:-3])

    for element in list_example:
        print(element)

    for index, element in enumerate(list_example):
        print(f"Index: {index} : element: {element}")

    example_rand = random.randint(1, 10)
    print(example_rand)

    for i in range(10):
        print(i)

    #  Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10. Wypisz listy na konosole raz z uzyciem petli
    #  drugi raz z uzyciem funkcji print
    random_list_1 = []
    random_list_2 = []
    for i in range(10):
        random_list_1.append(random.randint(1, 10))
        random_list_2.append(random.randint(1, 10))

    print(random_list_1)

    for index, element in enumerate(random_list_2):
        print(f'Presenting: {index} : {element}')

    ################################

    random_list_1[0] = 100

    list1 = [0, 1, 2]
    list2 = [3, 4, 5]

    for e in list2:
        list1.append(e)

    list1.extend(list2)
    print(list1)

    joined_list = list1 + list2
    print(joined_list)

    last_element = joined_list.pop()
    print(joined_list)
    print(f'Last element was: {last_element}')

    joined_list.remove(3)
    print(joined_list)

    random_list_3 = []
    for i in range(10):
        random_list_3.append(random.randint(1, 10))

    random_list_4 = [random.randint(1, 10) for i in range(10)]
    print(random_list_4)

    # Napisz kod który umieści w liście 10 kolejnych potęg liczby 2 uzywajac list składanych. 2 ** 2 = 4, 2 ** 3 = 8
    power_of_2 = [2 ** i for i in range(10)]
    print(power_of_2)

    power_of_2 = [(i, 2 ** i) for i in range(10)]
    print(power_of_2)

    ################################

    list1 = [0, 1, 2]
    list2 = [3, 4, 5]

    list_of_lists = [list1, list2]
    print(list_of_lists)

    zero_value = list_of_lists[0][0]
    print(zero_value)
    list_of_lists_of_lists = [[[1, 3], [3, 4]], [[32, 43]]]

    guest_list = ["Michael Scofield", "Lincoln Burrows", "TheodoreBagwell", "Uczciwy Polityk", "Andrzej Klusiewicz"]
    if "Lincoln Burrows" in guest_list:
        print("Found")
    else:
        print("Ooops not here")

    random_list_comp_2 = [random.randint(1, 10) for i in range(10)]
    print(f'Przed sortowaniem: {random_list_comp_2}')
    random_list_comp_2.sort()
    print(f'Po sortowaniu: {random_list_comp_2}')
    random_list_comp_2.reverse()
    print(f'Odwrotnie: {random_list_comp_2}')

    random_list_comp_3 = [random.randint(1, 10) for i in range(10)]
    posortowane = sorted(random_list_comp_3)
    odwrotnie = sorted(random_list_comp_3, reverse=True)
    print(posortowane)
    print(odwrotnie)

    filtered = [e for e in posortowane if e % 2 == 0]
    print(f"Only even {filtered}")

    # Napisz kod który połączy 2 listy podane poniżej, sprawdzi czy liczba 10 znajduje sie w nowej połączonej liście (wypisz odpowiedni komunikat),
    # a następnie posortuje te listę (bez tworzenia nowej). Następnie przefiltruja ta listę (tworząc nową) tak aby zawierała tylko liczby nieparzyste
    list1 = [3, 7, 1, 9, 15]
    list2 = [10, 2, 8, 6, 4]

    list1.extend(list2)
    if 10 in list1:
        print("Liczba 10 znajduje się w połączonej liście.")
    else:
        print("Liczba 10 nie znajduje się w połączonej liście.")
    list1.sort()

    odd_numbers = [num for num in list1 if num % 2 != 0]

    print(odd_numbers)


    napis = "Litery RoZnej WIelKOSCI"
    print(napis.lower())

    for root, dirs, files in os.walk('E:\PythonKurs_2_12_2024'):
        print(f'Root: {root}, folder: {dirs}, file: {files}')


    # Napisz wyszukiwarkę plików która
    # przyjmie od użytkownika szukaną frazę i katalog startowy. Wyszukiwarka ma wyswietlić
    # wszystkie pliki i katalogi zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
    # Wyszukiwarka ma być nieczuła na wielkość liter

    starting_folder = "E:\PythonKurs_2_12_2024"
    searched_text = ".Py"
    #searched_text = input()

    found = []
    searched_text = searched_text.lower()

    for root, dirs, files in os.walk(starting_folder):
        for element in dirs + files:
            if searched_text in element.lower():
                found.append(os.path.join(root, element))

    print(found)


    # searched_text = searched_text.lower()
    # found = [os.path.join(root, element)
    #          for root, dirs, files in os.walk(starting_folder)
    #          for element in dirs + files
    #          if searched_text in element.lower()]

    #############################

    list_5 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 12]

    print(f'Fours: {list_5.count(4)}')
    print(f'Index of 12: {list_5.index(12)}')
    list_5.clear()

    # Built in functions  len, sum, min, max
    list_6 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 12]

    len_of_list_6 = len(list_6)
    sum_of_list_6 = sum(list_6)
    min_of_list_6 = min(list_6)
    max_of_list_6 = max(list_6)
    print(f"Min: {min_of_list_6}, max: {max_of_list_6}, sum: {sum_of_list_6}")

    # revers with slicing [::-1]
    revers_6 = list_6[::-1]    # [start:stop:step]
    print(revers_6)

    every_second_element = list_6[::2]
    print(every_second_element)

    ############################### Krotki - tuple

    krotka = ("Wojtek", 30, 5.0)
    print(krotka)
    print(krotka[0])

    # krotka[0] = "Jan"


    def funkcje():
        return "wynik", 123, "sciezka"


    result = funkcje()
    print(f'Value: {result}, type: {type(result)}')

    napis, liczba, sciezka = funkcje()
    # napis, liczba, sciezka = result
    liczba += 1
    # result[1] += 1 # TypeError: 'tuple' object does not support item assignment

    krotka = tuple(random.randint(0, 10) for i in range(10))
    generator = (random.randint(0, 10) for i in range(10))  ### to nie jest krotka

    print(krotka)
    lista_z_krotki = list(krotka)
    print(lista_z_krotki)
    krotka_z_listy = tuple(lista_z_krotki)
    print(krotka_z_listy)


    # kopie glebokie listy
    list7 = list_6[::1] # kopia gleboka
    list7_copy = list(list_6) # kopia gleboka
    list7[0] = 100000

    print(list_6)
    print(list7)

    # bardziej skomplikowane struktury danych kopia gleboka
    import copy
    copy.deepcopy(list_of_lists_of_lists)

    # przyslanianie nazw
    # min = min(list_6)
    # min2 = min(list7_copy)