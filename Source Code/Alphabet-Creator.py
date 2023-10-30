import os
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def generate_random_name():
    name = ""
    for _ in range(20):
        name += random.choice(letters)
    return name.capitalize()

def generate_random_letter():
    name = ""
    for _ in range(2):
        name += random.choice(letters)
    return name.capitalize()

def create_new_alphabet():
    alphabet = {}
    print(" ")
    new_name = generate_random_name()
    print(" ")
    print(f"Alphabet Name: {new_name}")
    for i in range(26):
        new_letter = generate_random_letter()
        alphabet[letters[i]] = new_letter
        print(f"{i+1}. {new_letter}")

    print("\nExamples of using the new alphabet:")
    example_word = "hello"
    new_word = "".join([alphabet[char] for char in example_word])
    print(f"Original word: {example_word}")
    print(f"New alphabet word: {new_word.capitalize()}")

    print("\n1. Create New Alphabet")
    print("2. Exit")
    choice = input("Enter the number of your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            create_new_alphabet()
        elif choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exiting Application")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    else:
        print("You entered a string. Please enter a number.")

if __name__ == "__main__":
    create_new_alphabet()
