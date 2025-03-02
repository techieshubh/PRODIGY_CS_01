def caesar_cipher(text, shift, mode):
    result = ""
    
    # Determine the shift direction based on the mode
    if mode == 'decrypt':
        shift = -shift
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it unchanged
            result += char
    
    return result

def main():
    # Get user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    
    # Validate the mode
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    # Perform the encryption or decryption
    result = caesar_cipher(message, shift, mode)
    
    # Display the result
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
    
