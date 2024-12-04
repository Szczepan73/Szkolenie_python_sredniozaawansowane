def _validate_data(height: float, weight: float):
    if not (1.00 < height < 2.50 and weight < 200):
        raise ValueError("Invalid height or weight")


def calculate_bmi(height: float, weight: float) -> float:
    """
    Funckja liczaca BMI dla podanych parametrow
    Parameters
    ----------
    height: float wzrost w cm
    weight: waga w kg

    Returns
    -------
    Wyliczona wartosc BMI jako float
    """
    _validate_data(height, weight)
    return weight / (height / 100) ** 2