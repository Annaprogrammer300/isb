import json
from enum import Enum


class SerializeMethod(Enum):
    SERIALIZE_SYMMETRIC_KEY = 1
    DESERIALIZE_SYMMETRIC_KEY = 2


class SerializeMethodAsymmetric(Enum):
    SERIALIZE_PUBLIC_KEY = 1
    SERIALIZE_PRIVATE_KEY = 2
    DESERIALIZE_PUBLIC_KEY = 3
    DESERIALIZE_PRIVATE_KEY = 4


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
        :rtype: object
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


def read_config(config_file) -> dict:
    """
   Reads the configuration config from the specified file.

   Parameters:
        config_file : The path to the config file.

   Returns:
        dict: The configuration config loaded from the file.
   """

    try:
        with open(config_file, "r") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"config file '{config_file}' not found.")
    except Exception as e:
        print(f"Error reading config file: {str(e)}")


def write_config(config_file, config) -> None:
    """
    Writes the configuration config to the specified file.

    Parameters:
        config_file : The path to the config file.
        config : The configuration config to be written to the file.

    """
    try:
        with open(config_file, "w") as file:
            json.dump(config, file)
    except Exception as e:
        print(f"Error writing config file: {str(e)}")
