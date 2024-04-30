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

def identify_hash(hash_value):
    possible_types = []
    for name, algorithm in algorithms:
        try:
            if algorithm == "crc32" and zlib.crc32(hash_value.encode('utf-8')) == int(hash_value, 16):
                possible_types.append(name)
            elif hashlib.new(algorithm, hash_value.encode('utf-8')).hexdigest() == hash_value:
                possible_types.append(name)
        except ValueError:
            pass
    return possible_types

def decrypt_hash(hash_value, choice):
    if choice.isdigit() and 1 <= int(choice) <= len(algorithms):
        algorithm = algorithms[int(choice) - 1][1]
        if algorithm == "crc32":
            return zlib.crc32(hash_value.encode('utf-8'))
        else:
            hasher = getattr(hashlib, algorithm, None)
            if hasher:
                return hasher(hash_value.encode('utf-8')).hexdigest()
            else:
                return None
    else:
        return None

def main():
    user_input = input("Enter hash for attempted decryption (or hash, choice): ").strip()

    hash_value, choice = user_input.split(',') if ',' in user_input else (user_input, None)

    possible_types = identify_hash(hash_value)
    if possible_types:
        print("Possible hash types:")
        for idx, hash_type in enumerate(possible_types, start=1):
            print(f"{idx}. {hash_type}")
        
        if choice is not None:
            decrypted_hash = decrypt_hash(hash_value, choice)
            if decrypted_hash:
                print(f"Decrypted hash (using {possible_types[int(choice) - 1]}): {decrypted_hash}")
            else:
                print("Decryption failed.")
        else:
            for idx, hash_type in enumerate(possible_types[:5], start=1):
                print(f"Attempting decryption using {hash_type}...")
                decrypted_hash = decrypt_hash(hash_value, str(idx))
                if decrypted_hash:
                    print(f"Decrypted hash: {decrypted_hash}")
                else:
                    print("Decryption failed.")
                print()
    else:
        print("No possible hash types found.")

if __name__ == "__main__":
    main()
