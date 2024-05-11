import argparse

from asymmetric import AsymmetricEncryption
from symmetric import SymmetricEncryption
from works_files import write_bytes, read_bytes, SerializeMethod, SerializeMethodAsymmetric, read_config, Action


def handle_action(action: Action, symmetric: SymmetricEncryption, asymmetric: AsymmetricEncryption,
                  config: dict) -> bytes:
    """
    Handles the specified action by calling the corresponding function.

    Parameters:
        action (Action): The action to be performed.
        symmetric (SymmetricEncryption): An instance of the SymmetricEncryption class.
        asymmetric (AsymmetricEncryption): An instance of the AsymmetricEncryption class.
        config (dict): A dictionary containing the necessary configuration settings.

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
                symmetric.encrypt(config["data_file"], config["encrypted_file"])
            else:
                print("Error: Symmetric key is not in bytes format")
        case Action.DECRYPT:
            symmetric.key_operations(config["symmetric_key"], SerializeMethod.DESERIALIZE_SYMMETRIC_KEY)
            symmetric.decrypt(config["encrypted_file"], config["decrypted_file"])
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


