
from . import logger


def times3(a: float) -> float:
    logger.warn("Tutaj loguje na konsole z loggera z __init__.py")
    return a * 3


def _times4(a: float) -> float:
    return a * 4
