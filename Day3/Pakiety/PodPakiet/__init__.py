
print("Hello world from __init__.py")

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



__author__ = "Wojciech"

__doc__ = "Tu wpiszemy dokumentacje modułu"

from .functions import times3

__all__ = ["times3"]