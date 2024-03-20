#Symmetric-key Encryption:
#message is encoded and decoded with the same key
from cryptography.fernet import Fernet

message = "Hello World!"

key = Fernet.generate_key()

fernet = Fernet(key)

encrypted = fernet.encrypt(message.encode())

print('original message: ', message)
print('encrypted message: ', encrypted)

decrypted = fernet.decrypt(encrypted).decode()

print('decrypted message: ', decrypted)