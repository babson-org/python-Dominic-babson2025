# ==============================
# Main Program
# ==============================
def main():
    #Lists the options for the program
    while True:
        print("Lab 1 - Python Basics")
        print("1. Draw Diamond")
        print("2. Text Analysis")
        print("3. Caesar Cipher")
        choice = input("Select part to run (1-3): ")
        #runs the selcted function
        if choice == "1":
            draw_diamond()
        elif choice == "2":
            text_analysis()
        elif choice == "3":
            caesar_cipher()
        else:
            exit()

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    # Prompt user for an odd number, and checks to see if the user put in an integer
    while True:
        try:
            height = int(input("Enter an odd number for the diamond height: "))
            if height % 2 == 0:
                print("That wasn't an odd number. Please enter an odd number: ")
            else:
                break
        except ValueError: 
            print("That wasn't an integer. Please eneter an integer: ")
    # Draws the top half of the diamond
    # Calculates the spaces before the first star
    startSpaces = height//2
    # Iterates through desried length and prints "*" and spaces
    for i in range(startSpaces, -1, -1):
        before = " " * i
        betweenNum = ((startSpaces - i) * 2 - 1)
        between = " " * betweenNum
        if betweenNum == -1:
            print(before + "*")
        else:
            print(before + "*" + between + "*")
    # Draws the bottom half of the diamond by iterating similarly to the top
    for i in range(1, startSpaces + 1):
        before = " " * i
        betweenNum = ((startSpaces - i) * 2 - 1)
        between = " " * betweenNum
        if betweenNum == -1:
            print(before + "*")
        else:
            print(before + "*" + between + "*")

# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    # Get user input
    text = input("Enter some text: ")
    # Counts the letters using .isalpha()
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
        else:
            pass
    print(letters)
    # Counts the words by counting the spaces
    words = 1
    for space in text:
        if space == " ":
            words += 1
        else:
            pass
    #Counts the sentences with punctuation
    sent = 0
    for char in text:
        if char in ".?!":
            sent += 1
        else:
            pass
    # Print the results
    print(f"Letters: {letters}")
    print(f"Words: {words}")      
    print(f"Sentences: {sent}")    

# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    # Gets text, the shift amount, and if they want to encrypt or decrypt
    text = input("Enter text: ")
    shift = int(input("Enter shift value (integer): ")) % 26
    if input("Type 'e' to encrypt or 'd' to decrypt: ") == "d": 
        shift = -shift
    # Result will hold the result and alphabet holds all of the letters in the alphabet
    result = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Shifts by the number that the user inputs and maintains uppercase and lowercase in results
    for char in text:
        if char.islower():
            result += alphabet[(alphabet.index(char) + shift) % 26]
        elif char.isupper():
            result += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
        else: 
            result += char
    print("Result:", result)

if __name__ == "__main__":
    main()