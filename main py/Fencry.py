import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    return encrypted_data

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypted_data = encrypt_file(file_path, key)

            encrypted_file_path = file_path + '.enc'
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            # Save the key in FKeys folder
            parent_folder = os.path.dirname(os.path.abspath(__file__))
            key_folder = os.path.join(parent_folder, 'FKeys')
            if not os.path.exists(key_folder):
                os.makedirs(key_folder)
            key_name = os.path.relpath(file_path, folder_path).replace(os.path.sep, '_') + '_key.txt'
            key_file_path = os.path.join(key_folder, key_name)
            with open(key_file_path, 'wb') as key_file:
                key_file.write(key)

            # Delete the original file
            os.remove(file_path)

def main():
    path = input("Enter the path of the folder or file to encrypt: ")

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
        key_name = file_name.replace(os.path.sep, '_') + '_key.txt'
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

if __name__ == "__main__":
    main()
