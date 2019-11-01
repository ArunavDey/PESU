import os
from getpass import getpass as GP
from Crypto.Cipher import AES
from Crypto import Random
from login import setpass
"""LOGIN AS ADMIN """	
#read byte from file
with open('password.enc','rb') as file:
	ctext=file.read()
	file.close()
with open('key.txt','rb') as file:
	key=file.read()
	file.close()
with open('iv.txt','rb') as file:
	iv=file.read()	
	file.close()
#create a decipher to decrypt ciphertext
decipher=AES.new(key,AES.MODE_CFB,iv) 
plaintext=decipher.decrypt(ctext)
import time
def loginasadmin():
	global plaintext
	passwd=GP(prompt="Enter password for logging in:",stream=None)
	count=0
	while(passwd!=plaintext.decode('utf-8')):
		count+=1
		if(count==3):
			print("You entered wrong password 3 times.Try again in 60 seconds")
			time.sleep(60)
			count=0
			passwd=GP(prompt="Enter password again:",stream=None)
			continue
		passwd=GP(prompt="Invalid entry! Enter password again:",stream=None)
	#login successfull
	print("Successfully logged in")
def changepass():
	global plaintext
	passwd=GP(prompt="Enter older password:",stream=None)
	while(passwd!=plaintext.decode('utf-8')):
		passwd=GP(prompt='Invalid entry!enter original password again:',stream=None)
	#changepassword
	newpasswd=GP(prompt="Enter new password:")
	confnewpasswd=GP(prompt="Confirm the password:")
	while(newpasswd!=confnewpasswd):
		option=int(input('1.to confirm password again\n2.to set another password'))
		if(option==1):
			confnewpasswd=GP(prompt="Confirm the password:")
		elif(option==2):
			newpasswd=GP(prompt="Enter new password:")
			confnewpasswd=GP(prompt="Confirm the password:")
		else:
			continue
	#newpasswordset
	setpass(newpasswd)
	print('new password set successfully!')
	n=0
	while(n!=1 and n!=2)
	n=int(input('do you want to login now(press 1)\ndo you want to again change password(press 2)')
	if n==1:
		loginasadmin()
	elif n==2:
		changepass()	
while(choice!=1 and choice!=2)
	choice=int(input('for logging in as admin(press1)\nfor changing admin password(press2)')
	if(choice==1):
		loginasadmin()
	elif(choice==2):
		changepass()



	
	
	
	


