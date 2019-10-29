import os
from getpass import getpass as GP
from Crypto.Cipher import AES
from Crypto import Random
import pathlib
#prompts password,default prompt if not specified
path = pathlib.Path('password.enc')
if(path.exists()==False):
	password=GP(prompt="Set admin password:",stream=None)
	key=bytes(os.urandom(16))
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
#create a decipher to decrypt ciphertext
decipher=AES.new(key,AES.MODE_CFB,iv) 
#open the file in read mode
with open('password.enc','rb') as file:
	ctext=file.read()
	file.close()
#loginasadmin
import time
#read byte from file
plaintext=decipher.decrypt(ctext)
passwd=GP(prompt="Enter password for logging in:",stream=None)
count=0
while(passwd!=plaintext.decode('utf-8')):
	count+=1
	if(count==3):
		print("You entered wrong password 3 times.Try again in 60 seconds")
		time.sleep(60)
		count=0
		print("Enter password again")
		continue
	passwd=GP(prompt="Invalid entry!Enter password again",stream=None)
print("Successfully logged in")



