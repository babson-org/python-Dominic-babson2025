  text = input("Enter text: ")
    shift = int(input("Enter shift value (integer): ")) % 26
    if input("Type 'e' to encrypt or 'd' to decrypt: ") == "d": 
        shift = -shift
    result = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in text:
        if char.islower():
            result += alphabet[(alphabet.index(char) + shift) % 26]
        elif char.isupper():
            result += alphabet[(alphabet.index(char.lower()) + shift) % 26].upper()
        else: 
            result += char
    print("Result:", result)
