import argparse

from asymmetric import AsymmetricEncryption
from symmetric import SymmetricEncryption
from works_files import write_bytes, read_bytes, SerializeMethod, SerializeMethodAsymmetric, read_config, Action


def handle_action(action: Action, symmetric: SymmetricEncryption, asymmetric: AsymmetricEncryption,
                  config: dict) -> bytes:
    """
    Handles the specified action by calling the corresponding function.

    Parameters:
        action: The action to be performed.
        symmetric: An instance of the SymmetricEncryption class.
        asymmetric: An instance of the AsymmetricEncryption class.
        config: A dictionary containing the necessary configuration settings.

    Returns:
        bytes: The decrypted symmetric key if no decrypted key is returned.
    """
    match action:
        case Action.GENERATE_KEYS:
            asymmetric.generate_keys()
            asymmetric.key_operations(config["public_key"], SerializeMethodAsymmetric.SERIALIZE_PUBLIC_KEY)
            asymmetric.key_operations(config["private_key"], SerializeMethodAsymmetric.SERIALIZE_PRIVATE_KEY)
            symmetric.generate_key()
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.SERIALIZE_SYMMETRIC_KEY)
        case Action.ENCRYPT:
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.DESERIALIZE_SYMMETRIC_KEY)
            if isinstance(symmetric.key, bytes):
                symmetric.encrypt(config["data_text"], config["encrypted_text"])
            else:
                print("Error: Symmetric key is not in bytes format")
        case Action.DECRYPT:
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.DESERIALIZE_SYMMETRIC_KEY)
            symmetric.decrypt(config["encrypted_text"], config["decrypted_text"])
        case Action.ENCRYPT_SYMMETRIC_KEY:
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.DESERIALIZE_SYMMETRIC_KEY)
            asymmetric.key_operations(config["public_key"], SerializeMethodAsymmetric.DESERIALIZE_PUBLIC_KEY)
            symmetric_key = symmetric.key
            encrypted_symmetric_key = asymmetric.encrypt(symmetric_key)
            write_bytes(config["encrypted_symmetric_key"], encrypted_symmetric_key)
        case Action.DECRYPT_SYMMETRIC_KEY:
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.DESERIALIZE_SYMMETRIC_KEY)
            asymmetric.key_operations(config["private_key"], SerializeMethodAsymmetric.DESERIALIZE_PRIVATE_KEY)
            encrypted_symmetric_key = read_bytes(config["encrypted_symmetric_key"])
            decrypted_symmetric_key = asymmetric.decrypt(encrypted_symmetric_key)
            symmetric.key_operations(config["decrypted_symmetric_key"], SerializeMethod.SERIALIZE_SYMMETRIC_KEY)
            return decrypted_symmetric_key


def menu():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Starts the key generation mode')
    group.add_argument('-enc', '--encryption', help='Starts the encryption mode')
    group.add_argument('-dec', '--decryption', help='Starts the decryption mode')
    group.add_argument('-enc_sym', '--encryption_symmetric', help='Starts symmetric key encryption mode')
    group.add_argument('-dec_sym', '--decryption_symmetric', help='Starts symmetric key encryption mode')
    parser.add_argument("config", type=str, help="Path to the json file with the config")

    args = parser.parse_args()
    config = read_config(args.config)

    symmetric = SymmetricEncryption()
    asymmetric = AsymmetricEncryption()
    match args:
        case args if args.generation:
            handle_action(Action.GENERATE_KEYS, symmetric, asymmetric, config)
        case args if args.encryption:
            handle_action(Action.ENCRYPT, symmetric, asymmetric, config)
        case args if args.decryption:
            handle_action(Action.DECRYPT, symmetric, asymmetric, config)
        case args if args.encryption_symmetric:
            handle_action(Action.ENCRYPT_SYMMETRIC_KEY, symmetric, asymmetric, config)
        case args if args.decryption_symmetric:
            handle_action(Action.DECRYPT_SYMMETRIC_KEY, symmetric, asymmetric, config)
        case _:
            print("The wrong flag is selected")


if __name__ == "__main__":
    menu()
