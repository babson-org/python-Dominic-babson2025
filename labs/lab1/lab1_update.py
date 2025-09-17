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
'''
The draw_diamond function allows the user to enter an odd number form 1-9 and prints out 
a diamond basde on what the user prompts. The main challenge with this section of the code 
is that you must find the pattern with the starting spaces and the between spaces. To print
the bottom half of the diamond it is relatively similar to the top half, the only difference 
is the index of the for loop. 
'''
def draw_diamond():
    # Prompt user for an odd number, and checks to see if the user put in an integer
    while True:
        try:
            height = int(input("Enter an odd number for the diamond height: "))
            if height % 2 == 0:
                print("That wasn't an odd number. Please enter an odd number: ")
            elif height < 1 or height > 9:
                print("That number wasn't between 1 and 10. Please enter a different number: ")
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
'''
This section of the project takes a user's input and counts the number of
letters, words, and sentences that they input. This was a relatively 
simple section of the project. When creating the section to count the letters
you use the isalpha() built in function. To count the words you need to count the 
spaces in a sentence plus one. And to count the number of sentences you just count 
the number of times that sentence-ending punctuation is used. 
'''
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
'''
This section of the project takes input from the user and encrypts or decrypts it using the Caesar
Cipher. The cipher takes a number of letters that the user wants to shift their input by and sifts it
by that number of letters in the alphabet. I did this by listing out the alphabet (giving each value an index)
and then I assigned each new character by the old index + the shifted value. The decryption method works the same
way that the encryption does, it just shifts the values back by the shifted value rather than adding to it. 
A challenge of creating the caesar Cipher is wrapping it around the alphabet, because there are only 26 options. 
In order to combat this you must use % 26, giving the remainder above the alphabet when used.
'''
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