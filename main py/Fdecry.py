import os
import sys
from cryptography.fernet import Fernet

def load_key(key_path=None):
    if key_path:
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    else:
        parent_folder = os.path.dirname(os.path.abspath(__file__))
        key_folder = os.path.join(parent_folder, 'FKeys')
        key_files = [f for f in os.listdir(key_folder) if os.path.isfile(os.path.join(key_folder, f))]
        if key_files:
            key_file = os.path.join(key_folder, key_files[0])
            with open(key_file, 'rb') as default_key_file:
                return default_key_file.read()
        else:
            print("No key found in the default folder. Please provide the key or path of the key.")
            sys.exit(1)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data

def main():
    file_path = input("Enter the path of the file to decrypt: ")

    if not os.path.exists(file_path):
        print("Error: The provided file path does not exist.")
        sys.exit(1)

    key_input = input("Enter the path of the key file or leave blank to use default key folder: ")
    key = load_key(key_input)

    decrypted_data = decrypt_file(file_path, key)

    decrypted_file_path = os.path.splitext(file_path)[0]  # Remove .enc extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Decryption completed.")

    # Delete the encrypted file after successful decryption
    os.remove(file_path)

if __name__ == "__main__":
    main()
