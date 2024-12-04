import random
import requests  # pip install requests

# pip install pytest
# pip install pytest-cov


# https://docs.pytest.org/en/stable/

def sumuj(a: float, b: float) -> float:
    return a + b


def dajCyfry() -> list[int]:
    return list(range(1, 11))


# "kajak" true
# ""
# "kajak    " true
# "to nie jest palindromem" false
def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy dany ciąg znaków jest palindromem.

    Parameters:
        text (str): Ciąg znaków do sprawdzenia.

    Returns:
        bool: True, jeśli ciąg jest palindromem, False w przeciwnym razie.
    """
    text = text.lower().replace(" ", "")
    return (
        text == text[::-1]
    )


# napiszcie testy (pytest) ktore sprawdza czy potrafimy wyliczyc srednia
# osobny test dla pustej listy (dla None porownanie operatorem is)
def calculate_average(numbers: list[float]) -> float | None:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def calculate_percentage(value: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    return value * (percent / 100)


def nieprzetestowana_funckja(a):
    if a > 10:
        print(f"Hahahahaha a mnie nie przetestowałeś! {a}")
    print(f"Testing")

# pytest --cov=Day3 --cov-report=html
# pytest -v
# pytest -k "palindrome"
# pytest -m podstawowe
# pytest -s # przekierowanie std out na konsole


# napiszcie testy z uzyciem dekoratora parametrize do tej funkcji
def is_even(n):
    """
    Funkcja sprawdzająca, czy liczba jest parzysta.
    Zwraca True, jeśli liczba jest parzysta, False w przeciwnym przypadku.
    """
    return n % 2 == 0