def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("=" * 30)
        print(" Agent RXD's Caesar Cipher Tool")
        print("=" * 30)
        print("Menu:")
        print("                   ")
        print("1.  Encrypt text")
        print("2.  Decrypt text")
        print("3.  Exit")
        print("           ")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("=" * 30)
            plaintext = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(plaintext, shift)
            print("=" * 30)
            print("Encrypted text:", encrypted_text)
        elif choice == "2":
            print("=" * 30)
            encrypted_text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(encrypted_text, shift)
            print("=" * 30)
            print("Decrypted text:", decrypted_text)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
