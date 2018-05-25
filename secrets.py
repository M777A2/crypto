from crypto import Crypto
import sys

crypto = Crypto()


if len(sys.argv) < 2:
	msg = input("enter a message: ")
elif sys.argv[1][-4:] == ".txt":
	file = open(sys.argv[1])
	msg = file.read()
else:
	msg = sys.argv[1]

key = input("enter a key: ")
key = key.encode('utf-8')
key = key.hex()
key += "0"*(64-len(key))

mode = input("encrypt or decrypt? (e/d): ")
mode = mode[0]


if mode == "e":
	msg = crypto.symmetric_encrypt(msg, key, "AES")
elif mode == "d":
	msg = crypto.symmetric_decrypt(msg, key, "AES")

if input("Do you want to save as text?") in ['y','Y','yes','YES','Yes']:
	filename = input("enter a name for the file: ")
	file = open(filename, 'w')
	file.write(msg)
	file.close()
print(msg)
