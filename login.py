import os
from getpass import getpass as GP
from Crypto.Cipher import AES
from Crypto import Random
import pathlib 
path = pathlib.Path('password.enc')
def setpass():
	global password
	#prompts password,default prompt if not specified
	password=GP(prompt="Set admin password:",stream=None)
	#use os.urandom() method to create a random 16 bytes string
	#convert to bytes.
	key = bytes(os.urandom(16))
	#To generate an initializing vector, fixed block size is 16 bytes.
	iv = Random.new().read(AES.block_size)
	#Create a cipher to use for encryption
	cipher = AES.new(key,AES.MODE_CFB,iv)
	#encrypting password
	ciphertext=cipher.encrypt(password)
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
	setpass()	
#to store email id of admin incase password is lost
def storem():
	email=input('enter admin email id to be stored')
	with open('email.txt','w') as file:
		file.write(email)
		file.close()
path1=pathlib.Path('email.txt')
if(path1.exists()==False):
	storem()		
	
	
