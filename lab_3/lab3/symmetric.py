import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from works_files import (write_files, SerializeMethod, serialize_symmetric_key,
                         deserialize_symmetric_key, write_bytes, read_bytes)


class SymmetricEncryption:
    """
    A class that implements symmetric encryption using the IDEA algorithm.

    Attributes:
        key: encryption key
    """

    def __init__(self):
        self.key = None

    def generate_key(self) -> bytes:
        """
        Generates a random 16 byte encryption key.

        Returns
            The generated encryption key.
        """
        self.key = os.urandom(16)
        return self.key

