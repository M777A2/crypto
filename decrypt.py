from crypto import Crypto
import sys
C = Crypto()

filename = sys.argv[1]
file = open(filename, "r")
encrypted_msg = file.read()
file.close()

key = input("Enter a password(in hex): ")

key += "0"*(64-len(key))

iv = encrypted_msg[-32:]
encrypted_msg = encrypted_msg[:-32]

msg = C.symmetric_decrypt(encrypted_msg, key, "AES", "CBC", iv)

print(msg)
enc_file = open("enc" + filename, "w")
enc_file.write(msg)
enc_file.close()