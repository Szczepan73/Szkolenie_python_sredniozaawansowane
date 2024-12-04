from collections.abc import Iterator

from Day2.classes_and_objects import Zawodnik

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)

class IncrementIterator(Iterator):
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)

print("*" * 50)


nasz_iterator = IncrementIterator(5)

next(nasz_iterator)
next(nasz_iterator)
next(nasz_iterator)
print(next(nasz_iterator))



class MiesiaceIterator:
    def __init__(self):
        self.miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miesiace):
            miesiac = self.miesiace[self.indeks]
            self.indeks += 1
            return miesiac
        else:
            raise StopIteration

    def restart(self):
        self.indeks = 0


miesiace_iterator = MiesiaceIterator()

print("Miesiące:")
for i in range(12):
    print(next(miesiace_iterator))

miesiace_iterator.restart()
next(miesiace_iterator)

for i in range(11):
    print(next(miesiace_iterator))





class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))


class TreeIterator:
    def __init__(self, root):
        self.stack = [root] if root else []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()

        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)

        return node.value


iterator = TreeIterator(tree)

for value in iterator:
    print(value)



import torch
from torch.utils.data import DataLoader, Dataset


# Definiujemy niestandardowy dataset
class MyDataset(Dataset):
    def __init__(self):
        self.data = torch.arange(10)  # Tworzymy proste dane od 0 do 9

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Tworzymy dataset
dataset = MyDataset()

# Używamy DataLoader, który tworzy iterator
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Iterujemy po DataLoader (wykorzystując iterator wbudowany w DataLoader)
for batch in dataloader:
    print(batch)




########################## Kiedy __iter__ nie zwraca self
class MyCollection:
    def __init__(self, items):
        self.items = items    # to jest lista

    def __iter__(self):
        return MyCollectionIterator(self.items)


class MyCollectionIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


# Tworzymy kolekcję
collection = MyCollection([1, 2, 3])

# Iterujemy po kolekcji
for item in collection:
    print(item)

# Iterujemy po kolekcji kolejny raz
for item in collection:
    print(item)


print("*" * 50)


# uzupełnic klase lista zwodnikow o metody __iter__ oraz __next__
class ListaZawodnikow:
    def __init__(self, path: str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))
        self.index = 0




nasza_lista = ListaZawodnikow("dane.txt")
for z in nasza_lista:
    print(z)