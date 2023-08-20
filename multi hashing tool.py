import hashlib

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

while True:
    print("                        ")
    print("="*30)
    print("Agent RXD's Hashing Tool")
    print("="*30)
    print("                        ")
    print("1.  MD5")
    print("2.  SHA-1")
    print("3.  SHA-256")
    print("4.  SHA-512")
    print("                    ")
    print("5.  Exit")
    print("            ")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter the text to hash: ")
        result = md5_hash(text)
        print("MD5 Hash:", result)
    elif choice == '2':
        text = input("Enter the text to hash: ")
        result = sha1_hash(text)
        print("SHA-1 Hash:", result)
    elif choice == '3':
        text = input("Enter the text to hash: ")
        result = sha256_hash(text)
        print("SHA-256 Hash:", result)
    elif choice == '4':
        text = input("Enter the text to hash: ")
        result = sha512_hash(text)
        print("SHA-512 Hash:", result)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
