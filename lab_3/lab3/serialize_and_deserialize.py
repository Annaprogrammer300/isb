from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives import serialization


def serialize_symmetric_key(self, path: str) -> None:
    """
           Serializes the encryption key to a file.

           Parameters
               path: The path to the file where the encryption key will be saved.
           """
    try:
        with open(path, 'wb') as key_file:
            key_file.write(self.key)
        print(f"The symmetric key has been successfully written to the file '{path}'.")
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")


def deserialize_symmetric_key(self, file_name: str) -> None:
    """
           Deserializes the encryption key from a file.
           Parameters
               file_name: The path to the file containing the encryption key.
           """
    with open(file_name, "rb") as file:
        self.key = file.read()
    try:
        with open(file_name, "rb") as file:
            self.key = file.read()
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")


def serialization_public(self, public_path: str) -> None:
    """
    Serializes the RSA public key to files.

    Parameters
        public_path: The path to the file where the public key will be saved.
    """
    public_key = self.public_key
    try:
        with open(public_path, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        print(f"The public key has been successfully written to the file '{public_path}'.")
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def serialization_private(self, private_path: str) -> None:
    """
    Serializes the RSA private key to files.

    Parameters
        private_path: The path to the file where the private key will be saved.
    """
    private_key = self.private_key
    try:
        with open(private_path, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
            print(f"The private key has been successfully written to the file '{private_path}'.")
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def public_key_deserialization(self, public_path: str) -> None:
    """
    Deserializes the RSA public key from a file.

    Parameters
        public_path: The path to the file containing the public key.
    """
    try:
        with open(public_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
        self.public_key = load_pem_public_key(public_bytes)
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def private_key_deserialization(self, private_path: str) -> None:
    """
    Deserializes the RSA private key from a file.

    Parameters
        private_path: The path to the file containing the private key.
    """
    try:
        with open(private_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
        self.private_key = load_pem_private_key(private_bytes, password=None, )
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"Error: {str(e)}")