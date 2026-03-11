message = input("Enter message to encrypt: ")

encrypted = ""

for char in message:
    encrypted += chr(ord(char) + 3)

print("Encrypted message:", encrypted)

decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) - 3)

print("Decrypted message:", decrypted)