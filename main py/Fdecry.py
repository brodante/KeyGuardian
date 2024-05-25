"""
Author: Surya Pratap Singh Chauhan
GitHub: https://github.com/brodante
Email: surya.pratap0038@gmail.com
Website: https://brodante.github.io/portfolio/

Description: final year college student stuck in an infinite loop.
"""

import os
import sys
from cryptography.fernet import Fernet
import time

def logo():
    print("""\n
 ^ ^                 
(\033[96mO\033[0m,\033[96mO\033[0m)                
(   ) """+"by:\033[91m D4NT3 \033[0m"+"""    
▔"▔"▔▔▔▔▔▔▔▔▔▔▔▔""")

def load_key(key_path=None, file_path=None):
    if key_path:
        with open(key_path, 'rb') as key_file:
            return key_file.read()
    else:
        parent_folder = os.path.dirname(os.path.abspath(__file__))
        key_folder = os.path.join(parent_folder, 'FKeys')
        if os.path.isdir(file_path):
            folder_name = os.path.basename(file_path)
            key_file_name = folder_name + '_folder.key'
        else:
            file_name = os.path.basename(file_path)
            key_file_name = os.path.splitext(file_name)[0] + '_file.key'
        key_file_path = os.path.join(key_folder, key_file_name)
        if os.path.exists(key_file_path):
            with open(key_file_path, 'rb') as key_file:
                return key_file.read()
        else:
            print("No key found in the default folder. Please provide the key or path of the key.")
            time.sleep(3)
            sys.exit(1)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.enc'):
                file_path = os.path.join(root, file_name)
                decrypted_data = decrypt_file(file_path, key)

                decrypted_file_path = os.path.splitext(file_path)[0] # Remove .enc extension
                with open(decrypted_file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

                # Delete the encrypted file after successful decryption
                os.remove(file_path)

def Fdecry():
    logo()
    path = input("Enter the path of the file or folder to \033[96mDECRYPT\033[0m: ")

    if not os.path.exists(path):
        print("Error: The provided path does not exist.")
        time.sleep(3)
        sys.exit(1)

    key_input = input("Enter the path of the key file or leave blank to use default key folder: ")
    key = load_key(key_input, path)

    if os.path.isfile(path):
        # Decrypt single file
        decrypted_data = decrypt_file(path, key)

        decrypted_file_path = os.path.splitext(path)[0] # Remove .enc extension
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        for remaining in range(3, 0, -1):
            print(f"\033[96mDecryption completed\033[0m. Returning in \033[96m{remaining}...\033[0m", end="\r")
            time.sleep(1)  # Wait for 1 second

        # Delete the encrypted file after successful decryption
        os.remove(path)
    elif os.path.isdir(path):
        # Decrypt folder
        decrypt_folder(path, key)
        for remaining in range(3, 0, -1):
            print(f"\033[96mDecryption completed\033[0m. Returning in \033[96m{remaining}...\033[0m", end="\r")
            time.sleep(1)  # Wait for 1 second
    else:
        print("Error: The provided path is neither a file nor a directory.")
        time.sleep(3)
        sys.exit(1)

# if __name__ == "__main__":
#     main()
