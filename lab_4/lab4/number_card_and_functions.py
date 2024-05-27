import hashlib
import multiprocessing as mp
import time
from functools import partial
from typing import List
from works_files import read_json

from matplotlib import pyplot as plt
from tqdm import tqdm


def check_card_prefix(prefix: str, card_part: int, last_digit: int, target_hash: str) -> str:
    """
    Verifies if the given card part can form a valid card number.

    Parameters:
        prefix: The card number prefix (BIN).
        card_part: The part of the card number to check.
        last_digit: The last digit of the card number.
        target_hash: The hash value of the full card number to find a match for.
    Returns:
        The full card number if a match is found, otherwise an empty string.
    """
    card_number = f"{prefix}{str(card_part).zfill(6)}{last_digit}"
    if hashlib.sha3_224(card_number.encode()).hexdigest() == target_hash:
        return card_number
    return ""


def find_card_number(target_hash: str, card_prefixes: List[str],
                     last_digit: int, processes_count: int = mp.cpu_count()) -> str:
    """
    Finds the full card number by checking all possible combinations of the given parameters.

    Parameters:
        target_hash: The hash value of the full card number to find a match for.
        card_prefixes: A list of possible card number prefixes (BINs).
        last_digit: The last digit of the card number.
        processes_count: The number of processes to use for the search. Defaults to the number of CPUs available.
    Returns:
        The full card number if found, otherwise an empty string.
    """
    with mp.Pool(processes_count) as pool:
        partial_check_card_prefix = partial(check_card_prefix, target_hash=target_hash, last_digit=last_digit)
        for result in pool.starmap(partial_check_card_prefix,
                                   [(prefix, i) for prefix in card_prefixes for i in range(0, 999999)]):
            if result:
                print(f"The selected card number with {processes_count} processes: {result}")
                return result
    return ""


def validate_luhn(card_number: str) -> bool:
    """
    Validates a credit card number using the Luhn algorithm.

    Parameters:
        card_number: The credit card number to validate.
    Returns:
        True if the credit card number is valid, False otherwise.
    """
    digits = [int(digit) for digit in reversed(card_number)]
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = (digits[i] // 10) + (digits[i] % 10)
    return sum(digits) % 10 == 0


def plot_performance(target_hash: str, card_prefixes: List[str], last_digit: int) -> None:
    """
    Plots a graph of the execution time of the `find_card_number` function based on the number of processes used.

    Parameters:
        target_hash: The hash value of the full card number to find a match for.
        card_prefixes: A list of possible card number prefixes (BINs).
        last_digit: The last digit of the card number.
    """
    time_data = []
    for processes_count in tqdm(range(1, int(mp.cpu_count() * 1.5)), desc="Finding a collision"):
        start_time = time.time()
        if find_card_number(target_hash, card_prefixes, last_digit, processes_count):
            time_data.append(time.time() - start_time)

    plt.figure(figsize=(12, 6))
    plt.plot(range(1, int(mp.cpu_count() * 1.5)), time_data, color='#4CAF50', linestyle='-', marker='o', linewidth=2,
             markersize=8)
    plt.xlabel('Number of Processes')
    plt.ylabel('Execution Time (s)')
    plt.title('Card Number Search Performance')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    config = read_json("config_card.json")
    number = read_json("card.json")
    print(f"The card number is valid: {validate_luhn(number['number'])}")
    plot_performance(config["hash"], config["bins"], config["last_numbers"])
    find_card_number(config["hash"], config["bins"], config["last_numbers"])
