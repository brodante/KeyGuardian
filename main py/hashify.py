"""
Author: Surya Pratap Singh Chauhan
GitHub: https://github.com/brodante
Email: surya.pratap0038@gmail.com
Website: https://brodante.github.io/portfolio/

Description: final year college student stuck in an infinite loop.
"""

import hashlib
import zlib

# Define the algorithms and their corresponding codes
algorithms = [
    ("MD5 (Message Digest Algorithm 5)", "md5"),
    ("SHA-1 (Secure Hash Algorithm 1)", "sha1"),
    ("SHA-256 (Secure Hash Algorithm 256-bit)", "sha256"),
    ("SHA-512 (Secure Hash Algorithm 512-bit)", "sha512"),
    ("CRC-32 (Cyclic Redundancy Check 32-bit)", "crc32"),
    ("SHA-384 (Secure Hash Algorithm 384-bit)", "sha384"),
    ("CRC-16 (Cyclic Redundancy Check 16-bit)", "crc16"),
    ("Whirlpool", "whirlpool"),
    ("HMAC (Hash-based Message Authentication Code)", "hmac"),
    ("RIPEMD-160 (RACE Integrity Primitives Evaluation Message Digest 160-bit)", "ripemd160"),
    ("Tiger (Tiger hash function)", "tiger"),
    ("BLAKE2 (a cryptographic hash function)", "blake2b"),
    ("SHA-3 (Secure Hash Algorithm 3)", "sha3_256"),
    ("GOST (GOST hash function)", "streebog256"),
    ("NTLM (NT LAN Manager hash)", "ntlm"),
    ("LM (LAN Manager hash)", "lmhash"),
    ("PBKDF2 (Password-Based Key Derivation Function 2)", "pbkdf2_hmac"),
    ("Scrypt", "scrypt"),
    ("Argon2", "argon2"),
    ("bcrypt", "bcrypt")
]

def generate_hash(choice, data):
    algorithm = algorithms[int(choice) - 1][1]
    if choice == "5":
        return zlib.crc32(data.encode('utf-8'))
    elif choice == "6":
        return hashlib.sha384(data.encode('utf-8')).hexdigest()
    elif choice == "7":
        return zlib.crc32(data.encode('utf-8'), 0xffff)
    elif choice == "8":
        return hashlib.new('whirlpool', data.encode('utf-8')).hexdigest()
    else:
        hasher = getattr(hashlib, algorithm, None)
        if hasher:
            return hasher(data.encode('utf-8')).hexdigest()
        else:
            return None

def menu():
    print("\n#  Hash Menu:")
    print("▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔")
    for idx, (name, _) in enumerate(algorithms, start=1):
        print(f"{idx}. {name}")
    print("______________________________________________")
    print(f"0. or CTL+C Return to main menu")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def hashify():
    while True:
        try:
            menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Returning to main menu...")
                break

            if not choice.isdigit() or not (0 <= int(choice) <= len(algorithms)):
                print("Invalid choice! Please enter a valid option.")
                continue

            data = input("Enter the text: ")
            result = generate_hash(choice, data)
            print(f"{algorithms[int(choice) - 1][0]} Hash:", result)
        except KeyboardInterrupt:
                print("\n\n\tReturning to menu...")
                break  # Exit the loop and return to the calling function
