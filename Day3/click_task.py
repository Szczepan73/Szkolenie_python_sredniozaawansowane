# pip install click

import os
import click ### https://github.com/pallets/click


### opakowanie tej funkcji przy pomocy bibloteki click,
# katalog_startowy miał domyslna wartosc ".", fraza bedzie miała prompt, dopisz help do obu opcji

def znajdz_pliki_i_katalogi(katalog_startowy: str, fraza: str):
    """
    Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
    Parameters
    ----------
    katalog_startowy - katalog od ktorego zaczniemy przeszukiwanie
    fraza - fraza ktora jest wyszukiwana w nazwach plikow i katalogow

    Returns
    -------

    """
    znalezione_elementy = []

    fraza = fraza.lower()

    for root, dirs, files in os.walk(katalog_startowy):
        for element in dirs + files:
            if fraza in element.lower():
                znalezione_elementy.append(os.path.join(root, element))

    print(znalezione_elementy)


if __name__ == "__main__":
    znajdz_pliki_i_katalogi()

































































# @click.command()
# @click.option("--katalog_startowy", default=".", help="Katalog z ktorego zaczynamy przeszukiwac drzewo plikow")
# @click.option("--fraza", prompt="Czego szukasz:", help="Fragment nazwy ktorej szukasz")
# def znajdz_pliki_i_katalogi(katalog_startowy: str, fraza: str):
#     """
#     Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
#     Parameters
#     ----------
#     katalog_startowy - katalog od ktorego zaczniemy przeszukiwanie
#     fraza - fraza ktora jest wyszukiwana w nazwach plikow i katalogow
#
#     Returns
#     -------
#
#     """
#     znalezione_elementy = []
#
#     fraza = fraza.lower()
#
#     for root, dirs, files in os.walk(katalog_startowy):
#         for element in dirs + files:
#             if fraza in element.lower():
#                 znalezione_elementy.append(os.path.join(root, element))
#
#     print(znalezione_elementy)