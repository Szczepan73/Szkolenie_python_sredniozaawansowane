import pytest
import sys

from Day3.PyTest_examples.code_pytest import sumuj, dajCyfry, is_palindrome, calculate_average, calculate_percentage

def test_sumuj():
    assert sumuj(2,2) == 4


def test_dajCyfryMin():
    tab = dajCyfry()
    assert min(tab) == 1


def test_dajCyfryMax():
    tab = dajCyfry()
    assert max(tab) == 10


def test_dajCyfryLen():
    tab = dajCyfry()
    assert len(tab) == 10


def test_palindrome_true():
    assert is_palindrome("kajak") == True
    assert is_palindrome("kajak           ") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("racecar") == True


def test_palindrome_with_simple_palindromes():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True


def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("No lemon no melon") == True


def test_palindrome_with_mixed_case():
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("MadAm") == True


def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False


def test_empty_string():
    assert is_palindrome("") == True


def test_single_character():
    assert is_palindrome("a") == True
    assert is_palindrome("z") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == False  # Punctuation makes it not a palindrome in this implementation

def test_palindrome_with_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False



def test_average_empty_list():
    assert calculate_average([]) is None


def test_average_single_case():
    assert calculate_average([1, 2, 3]) == 2.0

# def test_average_single_case_2():
#     assert calculate_average([1, 2, 3 ,2]) == 2.0


lista_przypadkow_testowych = ["hello", "python", "123456x"]
@pytest.mark.parametrize('text', lista_przypadkow_testowych)
def test_palindrome_false(text):
    assert is_palindrome(text) == False


lista_przypadkow_testowych2 = [("hello", False), ("python", False), ("123456x", False), ("Kajak", True)]
@pytest.mark.parametrize('text, result', lista_przypadkow_testowych2)
def test_palindrome_false_parametryzacja_z_wynikiem(text, result):
    assert is_palindrome(text) == result


@pytest.mark.parametrize("numbers, expected_result", [
    ([1, 2, 3], 2.0),
    ([0, 0, 0, 0], 0.0),
    ([10, 20, 30, 40, 50], 30.0),
])
def test_average_parametrized(numbers, expected_result):
    print("Hello world")
    assert calculate_average(numbers) == expected_result



def test_calculate_percentage_invalid_percent():
    with pytest.raises(ValueError) as e:
        calculate_percentage(100, -10)
    assert str(e.value) == "Percent must be between 0 and 100"


@pytest.mark.skipif(sys.platform == "win32", reason="Pomijany na Windows")
def test_not_on_windows():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 9), reason="Wymaga Pythona 3.9 lub wyższej")
def test_requires_python_39():
    assert True