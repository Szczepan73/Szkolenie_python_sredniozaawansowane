import time
import pytest


@pytest.mark.podstawowe
def test_inny():
    assert 4 == 4

@pytest.mark.podstawowe
def test_true():
    assert True


# @pytest.mark.podstawowe
# @pytest.mark.zaawansowane
# def test_czy_to_dziala():
#     assert 1 == 2
#
#
# @pytest.mark.wolne
# def test_dlugi():
#     time.sleep(5)
#     assert 1 == 1