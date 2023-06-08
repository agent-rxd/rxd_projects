import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def collect_details():

    website = input("Enter the website name: ")
    username = input("Enter the username/email: ")
    length = int(input("Enter the length of the password: "))
    
    
    password = generate_password(length)
    
    
    file_name = website + ".txt"
    with open(file_name, 'w') as file:
        file.write(f"Website: {website}\n")
        file.write(f"Username/Email: {username}\n")
        file.write(f"Password: {password}\n")
    
   
    print("Details and generated password exported to", file_name)
    print("Website:", website)
    print("Username/Email:", username)
    print("Generated Password:", password)
    print() 

def menu():
    print("Welcome to the Password Generator!")

    while True:
        print("1. Generate Password")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            collect_details()
        elif choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        print() 


menu()
