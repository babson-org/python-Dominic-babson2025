"""
Lab 1 – Python Basics
Author: <Your Name>
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

"""
if (height % 2 == 0):
    height = int(input("That wasn't an odd number. Please enter an odd number: "))
elif (height > 10):
    height = int(input("That was greater than 10. Please enter a number less than 10"))
"""





# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    """
    Ask the user for an odd number for the diamond height
    and print a symmetric diamond of that height.
    """
    # TODO: Prompt user for an odd number

while True:
    try:
        height = int(input("Enter an odd number for the diamond height: "))
    except: 
ValueError
        print("That wasn't an integer. Please eneter an integer")

    # TODO: Draw the top half of the diamond
startSpaces = height//2
for i in range(startSpaces, -1, -1):
    before = " " * i
    betweenNum = ((startSpaces - i) * 2 - 1)
    between = " " * betweenNum
    if betweenNum == -1:
        print(before + "*")
    else:
        print(before + "*" + between + "*")
    # TODO: Draw the bottom half of the diamond
for i in range(1, startSpaces + 1):
    before = " " * i
    betweenNum = ((startSpaces - i) * 2 - 1)
    between = " " * betweenNum
    if betweenNum == -1:
        print(before + "*")
    else:
        print(before + "*" + between + "*")
# Uncomment to test Part 1
# draw_diamond()


# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """
    # TODO: Get user input
text = input("Enter some text: ")
    # TODO: Count letters
letters = 0
for char in text:
    if char.isalpha():
        letters += 1
    else:
        pass
print(letters)
    # TODO: Count words
words = 1
for space in text:
    if space == " ":
        words += 1
    else:
        pass
print(words)
    # TODO: Count sentences
sentences = 0
for sent in text:
    if sent == "." | "!" | "?":
        sent += 1
    else:
        pass
print(sent)

    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {0}")        # replace 0
    print(f"Sentences: {0}")    # replace 0

# Uncomment to test Part 2
# text_analysis()


# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================
def caesar_cipher():
    """
    Ask the user for text and a shift value.
    Provide options to encrypt or decrypt the text using a Caesar cipher.
    """

    # TODO: Get user input text
    text = input("Enter text: ")

    # TODO: Get shift value
    shift = int(input("Enter shift value (integer): "))

    # TODO: Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    # TODO: Implement encryption and decryption logic
    result = ""
if result == "e":
    for i in range(len(text)):
        new_index = (i + shift) % len(text)
        result = result + result[i]
else:
    for i in range(len(text)):
        new_index = (i - shift) % len(text)
        result = result + result[i]

    # TODO: Print the final result
    print("Result:", result)

# Uncomment to test Part 3
# caesar_cipher()


# ==============================
# Main Program
# ==============================
def main():
    print("Lab 1 - Python Basics")
    print("1. Draw Diamond")
    print("2. Text Analysis")
    print("3. Caesar Cipher")
    choice = input("Select part to run (1-3): ")
    
    if choice == "1":
        draw_diamond()
    elif choice == "2":
        text_analysis()
    elif choice == "3":
        caesar_cipher()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
