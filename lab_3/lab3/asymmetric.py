from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from serialize_and_deserialize import (private_key_serialization,
                                       public_key_deserialization, private_key_deserialization,
                                       public_key_serialization)
from works_files import SerializeMethodAsymmetric


class AsymmetricEncryption:
    """
    A class that implements asymmetric encryption and decryption using the RSA algorithm.

    Attributes
        private_key: The private key.
        public_key: The public key.
    """

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self) -> None:
        """
        Generates a new RSA private and public key pair.
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.private_key = keys
        self.public_key = keys.public_key()

    def key_operations(self, path: str, method: SerializeMethodAsymmetric) -> None:
        """
        Performs key serialization or deserialization operations.

        Parameters:
            path: The path to the file containing or where the key will be stored.
            method: The serialization or deserialization method to use.
        """
        match method:
            case SerializeMethodAsymmetric.SERIALIZE_PUBLIC_KEY:
                public_key_serialization(path, self.public_key)
            case SerializeMethodAsymmetric.SERIALIZE_PRIVATE_KEY:
                private_key_serialization(path, self.private_key)
            case SerializeMethodAsymmetric.DESERIALIZE_PUBLIC_KEY:
                self.public_key = public_key_deserialization(path)
            case SerializeMethodAsymmetric.DESERIALIZE_PRIVATE_KEY:
                self.private_key = private_key_deserialization(path)

    def encrypt(self, symmetric_key: bytes) -> bytes:
        """
        Encrypts a symmetric key using the public key.

        Parameters:
            symmetric_key: The symmetric key to be encrypted.

        Returns:
            bytes: The encrypted symmetric key.
        """
        encrypted_symmetric_key = self.public_key.encrypt(symmetric_key,
                                                          padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                       algorithm=hashes.SHA256(), label=None))
        return encrypted_symmetric_key

    def decrypt(self, symmetric_key: bytes) -> bytes:
        """
        Decrypts a symmetric key using the private key.

        Parameters:
            symmetric_key: The encrypted symmetric key to be decrypted.

        Returns:
            bytes: The decrypted symmetric key.
        """
        decrypted_symmetric_key = self.private_key.decrypt(symmetric_key,
                                                           padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                        algorithm=hashes.SHA256(), label=None))
        return decrypted_symmetric_key
