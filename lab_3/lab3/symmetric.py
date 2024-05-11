import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from works_files import write_files


class Symmetric:
    """
    A class that implements symmetric encryption using the IDEA algorithm.

    """
