'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    Generates a random password based on the user's criteria.
    """
    character_pool = ""
    
    # Build the character pool based on complexity preferences
    if use_letters:
        character_pool += string.ascii_letters  # Contains both lowercase and uppercase letters
    if use_numbers:
        character_pool += string.digits         # Contains 0-9
    if use_symbols:
        character_pool += string.punctuation    # Contains special characters like !, @, #, $, etc.

    # If the user said 'no' to everything, return an error message
    if not character_pool:
        return "Error: You must select at least one character type!"

    # Generate a random password by picking random characters from the pool
    # The list comprehension runs 'length' times, and ''.join() merges them into a single string
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("=========================================")
    print("       SECURE PASSWORD GENERATOR         ")
    print("=========================================\n")
    
    # 1. User Input: Get and validate the desired length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("❌ Error: Password length must be greater than 0.")
            return
    except ValueError:
        print("❌ Error: Please enter a valid whole number for the length.")
        return

    # 2. User Input: Specify complexity
    print("\n--- Configure Password Complexity ---")
    include_letters = input("Include Letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include Special Characters/Symbols? (y/n): ").strip().lower() == 'y'

    # 3. Generate the password
    password = generate_password(length, include_letters, include_numbers, include_symbols)

    # 4. Display the generated password
    print("\n=========================================")
    print(f" Your Generated Password is:\n {password}")
    print("=========================================")

if __name__ == "__main__":
    main()