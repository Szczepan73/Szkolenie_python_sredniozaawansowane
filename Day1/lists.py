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