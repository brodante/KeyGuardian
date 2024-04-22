# main.py

import identifyhash

def identify_hash():
    hash_input = input("Enter the hash: ")
    identifyhash.identify_hash(hash_input)

def encrypt():
    # Implement encryption logic here
    print("Encryption function")

def decrypt():
    # Implement decryption logic here
    print("Decryption function")

def exit_program():
    print("Exiting...")
    exit()

def main():
    while True:
        print("\nMenu:")
        print("1. Identify Hash")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            identify_hash()
        elif choice == "2":
            encrypt()
        elif choice == "3":
            decrypt()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
