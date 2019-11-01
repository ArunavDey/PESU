import os
from getpass import getpass as GP
from Crypto.Cipher import AES
from Crypto import Random
import pathlib
#prompts password,default prompt if not specified
path = pathlib.Path('password.enc')
password=GP(prompt="Set admin password:",stream=None)
def setpass(p):
	#use os.urandom() method to create a random 16 bytes string
	#convert to bytes.
	key = bytes(os.urandom(16))
	#To generate an initializing vector, fixed block size is 16 bytes.
	iv = Random.new().read(AES.block_size)
	#Create a cipher to use for encryption
	cipher = AES.new(key,AES.MODE_CFB,iv)
	#encrypting password
	ciphertext=cipher.encrypt(p)
	#open create file named-password.enc
	#write bytes into file
	with open('password.enc','wb') as file:
		file.write(ciphertext)
		file.close()
	with open('key.txt','wb') as file:
		file.write(key)
		file.close()
	with open('iv.txt','wb') as file:
		file.write(iv)
		file.close()
if(path.exists()==False):
	setpass(password)	



