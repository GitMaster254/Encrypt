import rsa

publicKey, privateKey = rsa.newkeys(512)

message = "Hello World!"

encrypted = rsa.encrypt(message.encode(), publicKey)

print('original message: ', message)
print('encrypted message: ', encrypted)

decrypted = rsa.decrypt(encrypted, privateKey).decode()

print('decrypted message: ', decrypted)