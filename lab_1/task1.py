import os

from works_files import *

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя .,?/!()- \n "


def encrypt(path_key: str, text_path: str, path: str) -> None:
    """
    implements the atbash cipher and writes data to a file

    Parameters
        text_path: the path to the file where the message is located
        path: the path where the cipher will be written
    """
    key = read_json(path_key)
    result = ''
    text = read_files(text_path)
    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char
        write_files(path, result)
    else:
        print("Ошибка: Не удалось прочитать текст из файла.")


def decrypt(path_key: str, path_encryption: str, path_decryption: str) -> None:
    """
    implements the atbash cipher and writes data to a file

    Parameters
        text_path: the path to the file where the message is located
        path: the path where the cipher will be written
    """
    key = read_json(path_key)
    result = ''
    text = read_files(path_encryption)
    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char
        write_files(path_decryption, result)
    else:
        print("Ошибка: Не удалось прочитать текст из файла.")


def key_json(key: str, path: str) -> None:
    sz = len(key)  # Получаем размер ключа
    key = dict()
    num_rows = -(-len(alphabet) // sz)
    matrix = [['' for _ in range(sz)] for _ in range(num_rows)]

    index = 0
    for row in range(num_rows):
        for col in range(sz):  # Исправлено
            if index < len(alphabet):
                matrix[row][col] = alphabet[index]
                index += 1

    # Шифруем текст по столбцам согласно ключу
    ciphertext = ''
    for col in range(sz):
        for row in range(num_rows):
            ciphertext += matrix[row][col]

    for i, char in enumerate(alphabet):
        key[char] = ciphertext[i]
    write_json(key, path)


if __name__ == "__main__":
    keys = "43521"

    # Создание ключа для шифра и запись в файл
    key_json(keys, os.path.join('first_task', 'key.json'))

    encrypt(os.path.join('first_task', 'key.json'), os.path.join('first_task', 'text_path.txt'),
            os.path.join('first_task', 'encryption.txt'))
    decrypt(os.path.join('first_task', 'key.json'), os.path.join('first_task', 'encryption.txt'),
            os.path.join('first_task', 'decryption.txt'))
