"""
Author: Surya Pratap Singh Chauhan
GitHub: https://github.com/brodante
Email: surya.pratap0038@gmail.com
Website: https://brodante.github.io/portfolio/

Description: final year college student stuck in an infinite loop.
"""
# main.py
import os
import identifyhash
import hashify

def logo(): # https://patorjk.com/software/taag/#p=display&f=Big&t=KeyGuardian%20v0.04%20beta
    os.system("cls" if os.name == "nt" else "clear")
    #print("\n\n")
    print("\033[96m" + "{:^80}".format("KeyGuardian v0.04") + "\033[0m")
    print("\033[92m" + """
  _  __           _____                     _ _                      ___   ___  _  _     _          _        
 | |/ /          / ____|                   | (_)                    / _ \ / _ \| || |   | |        | |       
 | ' / ___ _   _| |  __ _   _  __ _ _ __ __| |_  __ _ _ __   __   _| | | | | | | || |_  | |__   ___| |_ __ _ 
 |  < / _ \ | | | | |_ | | | |/ _` | '__/ _` | |/ _` | '_ \  \ \ / / | | | | | |__   _| | '_ \ / _ \ __/ _` |
 | . \  __/ |_| | |__| | |_| | (_| | | | (_| | | (_| | | | |  \ V /| |_| | |_| |  | |   | |_) |  __/ || (_| |
 |_|\_\___|\__, |\_____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|   \_/  \___(_)___/   |_|   |_.__/ \___|\__\__,_|
            __/ |                                                                                            
           |___/                                                                                             
""" + "\033[0m")

def identify_hash():
    identifyhash.identify_hash()
def encrypt():
    hashify.hashify()
    #print("Encryption function")

def decrypt():
    # Implement decryption logic here
    print("Decryption function")

def exit_program():
    print("\nByeBye...")
    exit()

def main():
    while True:
        try:
            logo()
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
        except KeyboardInterrupt:
            print("\nByeBye...")
            exit()

if __name__ == "__main__":
    main()
