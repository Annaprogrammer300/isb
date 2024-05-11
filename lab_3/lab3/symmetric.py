import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from works_files import write_files, SerializeMethod, write_bytes, read_bytes
from serialize_and_deserialize import serialize_symmetric_key, deserialize_symmetric_key


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

    def key_operations(self, file_name: str, method: SerializeMethod) -> None:
        """
        Performs key serialization or deserialization operations.

        Parameters:
            file_name: The path to the file containing the encryption key.
            method: The serialization or deserialization method to use.
        """
        match method:
            case SerializeMethod.SERIALIZE_SYMMETRIC_KEY:
                serialize_symmetric_key(file_name, self.key)
            case SerializeMethod.DESERIALIZE_SYMMETRIC_KEY:
                self.key = deserialize_symmetric_key(file_name)

    def encrypt(self, path: str, encrypted_path: str) -> bytes:
        """
        Encrypts data from a file using the IDEA algorithm in CFB mode.

        Parameters
            path: The path to the file with the source data.
            encrypted_path: The path to the file where the encrypted data will be written.
        Returns
            The encrypted data.
        """
        text = read_bytes(path)
        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(self.key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        adder = padding.ANSIX923(32).padder()
        padded_text = adder.update(text) + adder.finalize()
        cipher_text = iv + encryptor.update(padded_text) + encryptor.finalize()
        write_bytes(encrypted_path, cipher_text)
        return cipher_text

    def decrypt(self, encrypted_path: str, decrypted_path: str) -> str:
        """
        Decrypts data from a file using the IDEA algorithm in CFB mode.

        Parameters
            encrypted_path: The path to the file with the encrypted data.
            decrypted_path: The path to the file where the decrypted data will be written.
        Returns
            The decrypted data as a string.
        """
        encrypted_text = read_bytes(encrypted_path)
        iv = encrypted_text[:8]
        cipher_text = encrypted_text[8:]
        cipher = Cipher(algorithms.IDEA(self.key), modes.CFB(iv))
        decrypt = cipher.decryptor()
        unpacker_text = decrypt.update(cipher_text) + decrypt.finalize()
        decrypt_text = unpacker_text.decode('UTF-8')
        write_files(decrypted_path, decrypt_text)
        return decrypt_text
