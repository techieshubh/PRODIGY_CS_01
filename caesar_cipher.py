def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        # for uppercase letters
        if char.isupper():
            start = ord('A')
            result += chr((ord(char) - start + (shift if action == "e" else -shift)) % 26 + start)
        # for lowercase letters
        elif char.islower():
            start = ord('a')
            result += chr((ord(char) - start + (shift if action == "e" else -shift)) % 26 + start)
        # for non-alphabet characters
        else:
            result += char
    return result

def main():
    print("Task 01 : Caesar Cipher Program")
    
    message = input("Enter your message: ")
    shift = int(input("Enter a positive shift value: "))
    
    # Choose encryption or decryption
    action = input("Do you want to encrypt or decrypt the message? (enter 'e' or 'd'): ").lower()
    
    while action not in ["e", "d"]:
        print("Invalid action. Please enter 'e' or 'd'.")
        action = input("Do you want to encrypt or decrypt the message? (enter 'e' or 'd'): ").lower()
    
    # Encrypt or decrypt the message
    result = caesar_cipher(message, shift, action)
    
    # Display the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
