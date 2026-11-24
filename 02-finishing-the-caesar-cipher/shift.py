ALPHABET_SIZE = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

ciphertext = ""

#Encryption Loop
for character in message:
    if "A" <= character <= "Z":                  # ALTERNATIVE: if character >= "A" and character <= "Z":
        shifted = ord(character) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    else:
        ciphertext += character 

print("Ciphertext:", ciphertext)

plaintext = ""


#Decryption Loop
for character in ciphertext:
    if "A" <= character <= "Z":                  # ALTERNATIVE: if character >= "A" and character <= "Z":
        shifted = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += character 

print("Plaintext:", plaintext)
assert plaintext == message, "Decrypted text does not match the original message"