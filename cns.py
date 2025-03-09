def caesar_cipher(text, shift):
    result = ""
    
    # Normalize shift to be within the range [0, 25]
    shift %= 26

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

def main():
    text = "Hello, World!"
    shift = 3
    
    encrypted = caesar_cipher(text, shift)
    print(f"Encrypted Text: {encrypted}")
    
    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Decrypted Text: {decrypted}")

if __name__ == "__main__":
    main()
