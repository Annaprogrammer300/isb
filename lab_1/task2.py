import os

from task1 import encrypt
from works_files import *


def frequency_analysis(text_path: str, path: str) -> None:
    """
    Performs a frequency analysis of the text and writes it to the dictionary in another file

    Parameters
        text_path: the path to the file with the text to analyze
        path: the path to the file where the frequency analysis will be recorded
    """
    text = read_files(text_path)
    frequencies = {}
    total = len(text)
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    for char, count in frequencies.items():
        frequencies[char] = count / total
    sort = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    write_json(sort, path)


def key_json(freq_path: str, path: str, data_path: str) -> None:
    """
    Create a key to the text based on statistical analysis of
    the text and data on frequently encountered characters and write
    it to a json file in the form of a dictionary

    Parameters
        freq_path: the path from which text statistical analysis data is taken
        paths: the path where the key will be written
        data_path: the path from which character data is taken
    """
    key = read_json(freq_path)
    result = {}
    alf = read_json(data_path)

    for key_char, value_char in zip(key.keys(), alf.values()):
        result[key_char] = value_char
        found_key = None
        for k, v in alf.items():
            if v == value_char:
                found_key = k
                break
        result[key_char] = found_key
    write_json(result, path)


if __name__ == "__main__":
    try:
        frequency_analysis(os.path.join('second_task', 'cod8.txt'), os.path.join('second_task', 'freq.json'))
        key_json(os.path.join('second_task', 'freq.json'), os.path.join('second_task', 'key.json'),
                 os.path.join('second_task', 'data.json'))
        encrypt(os.path.join('second_task', 'key.json'), os.path.join('second_task', 'cod8.txt'),
                os.path.join('second_task', 'decryption.txt'))
        encrypt(os.path.join('second_task', 'text_key.json'), os.path.join('second_task', 'cod8.txt'),
                os.path.join('second_task', 'text_decryption.txt'))
    except Exception as e:
        print(f"An error occurred: {e}")
