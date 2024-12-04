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