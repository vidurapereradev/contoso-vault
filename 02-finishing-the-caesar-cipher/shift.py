ALPHABET_SIZE = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext: str = ""

#Encryption Loop
#Upper Case Loop
for character in message:
    if "A" <= character <= "Z":                  # ALTERNATIVE: if character >= "A" and character <= "Z":
        shifted: int = ord(character) + key           # Shifting the character by the key value and then get the ASCII value of the shifted character
        if shifted > ord("Z"):                   # If the shifted character is greater than "Z", we need to wrap around to the beginning of the alphabet
            shifted -= ALPHABET_SIZE            
        ciphertext += chr(shifted)               # Converting the ASCII value back to a character and adding it to the ciphertext

    else:

        #Lower Case Loop
        if "a" <= character <= "z":                  
            shifted: int = ord(character) + key
            if shifted > ord("z"):
                shifted -= ALPHABET_SIZE
            ciphertext += chr(shifted)
        else:
         ciphertext += character 

print("Ciphertext:", ciphertext)

plaintext: str  = ""


#Decryption Loop
#Upper Case Loop
for character in ciphertext:
    if "A" <= character <= "Z":                  # ALTERNATIVE: if character >= "A" and character <= "Z":
        shifted: int = ord(character) - key      # Shifting the character by the key value and then get the ASCII value of the shifted character
        if shifted < ord("A"):                   # If the shifted character is less than "A", we need to wrap around to the end of the alphabet
             shifted += ALPHABET_SIZE
        plaintext += chr(shifted)                # Converting the ASCII value back to a character and adding it to the plaintext

    else:

        #Lower Case Loop
        if "a" <= character <= "z":                  
            shifted: int = ord(character) - key
            if shifted < ord("a"):
                shifted += ALPHABET_SIZE
            plaintext += chr(shifted)
        else:
            plaintext += character 

print("Plaintext:", plaintext)
assert plaintext == message, "Decrypted text does not match the original message" 