import json
from enum import Enum


class SerializeMethod(Enum):
    SERIALIZE_SYMMETRIC_KEY = 1
    DESERIALIZE_SYMMETRIC_KEY = 2


def write_files(path: str, data: str) -> None:
    """
    A function for writing data to a file.

    Parameters
        path: the path to the file to write
        data: data to write to a file
    """
    try:
        with open(path, "a", encoding='UTF-8') as file:
            file.write(data)
        print(f"The data has been successfully written to the file '{path}'.")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")


def read_json(path: str) -> dict:
    """
    A function for reading data from a JSON file and returning a dictionary.

    Parameters
        path: the path to the JSON file to read
    Returns
        Dictionary of data from a JSON file
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"The file '{path}' was not found")
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {str(e)}")


def read_bytes(file_path: str) -> bytes:
    """
    Reads the contents of a file in binary format.

    Parameters
        file_path: The path to the file to be read.
    Returns
        The contents of the file in binary format.
    """
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")


def write_bytes(file_path: str, bytes_text: bytes) -> None:
    """
    Writes binary data to a file.

    Parameters
        file_path: The path to the file where the data will be written.
        bytes_text: The binary data to be written to the file.
    """
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_text)
        print(f"The data has been successfully written to the file '{file_path}'.")
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")


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
