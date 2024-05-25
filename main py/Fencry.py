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

def logo():
    print("""\n
 ^ ^                 
(\033[96mO\033[0m,\033[96mO\033[0m)                
(   ) """+"by:\033[91m D4NT3 \033[0m"+"""    
▔"▔"▔▔▔▔▔▔▔▔▔▔▔▔""")

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    return encrypted_data

def encrypt_folder(folder_path, key):
    # Generate a single key for the folder
    key = generate_key()

    # Save the key in FKeys folder
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    key_folder = os.path.join(parent_folder, 'FKeys')
    if not os.path.exists(key_folder):
        os.makedirs(key_folder)
    # Naming the key file similar to the folder name followed by "_folder.key"
    folder_name = os.path.basename(folder_path)
    key_name = folder_name + '_folder.key'
    key_file_path = os.path.join(key_folder, key_name)
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

    # Encrypt each file in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypted_data = encrypt_file(file_path, key)

            encrypted_file_path = file_path + '.enc'
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            # Delete the original file
            os.remove(file_path)

def Fencry():
    logo()
    path = input("Enter the path of the folder or file to \033[91mENCRYPT\033[0m : ")

    # Check if the path is in the same directory as Fencry.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.dirname(os.path.abspath(path))
    if script_dir == target_dir:
        print("\033[91mWarning: Cannot encrypt files or folders in the same directory as Fencry.py.\033[0m")
        sys.exit(1)

    if not os.path.exists(path):
        print("Error: The provided path does not exist.")
        sys.exit(1)

    key = generate_key()
    if os.path.isfile(path):
        # Encrypt single file
        folder_path, file_name = os.path.split(path)
        encrypted_data = encrypt_file(path, key)

        encrypted_file_path = os.path.join(folder_path, file_name + '.enc')
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Save the key in FKeys folder
        parent_folder = os.path.dirname(os.path.abspath(__file__))
        key_folder = os.path.join(parent_folder, 'FKeys')
        if not os.path.exists(key_folder):
            os.makedirs(key_folder)
        key_name = file_name.replace(os.path.sep, '_') + '_file.key'
        key_file_path = os.path.join(key_folder, key_name)
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)

        # Delete the original file
        os.remove(path)
    elif os.path.isdir(path):
        # Encrypt folder
        encrypt_folder(path, key)
    else:
        print("Error: The provided path is neither a file nor a directory.")
        sys.exit(1)

    print("Encryption completed.")

# if __name__ == "__main__":
#     main()
