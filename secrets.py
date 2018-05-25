from crypto import Crypto

test = Crypto()

msg = "here is my bank account number: 1231872365471, Plz don't steal."

key = "DEADBEEF"
key += "0"*(64-len(key))
print(len(key))

encoded_msg = test.symmetric_encrypt(msg, key, "AES")

print(msg)
print(encoded_msg)



decoded = test.symmetric_decrypt(encoded_msg, key, "AES")

print(decoded)