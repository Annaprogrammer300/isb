from test import *

if __name__ == "__main__":
    try:
        config = read_json("config.json")
        text_to = config["to"]
        text_from = config["from"]

        frequency_test(text_from, text_to, "java")
        frequency_test(text_from, text_to, "cpp")

        same_bits_test(text_from, text_to, "java")
        same_bits_test(text_from, text_to, "cpp")

        longest_sequence_in_block_test(text_from, text_to, "java")
        longest_sequence_in_block_test(text_from, text_to, "cpp")
    except Exception as e:
        print(f"An error occurred during the main execution: {e}")
