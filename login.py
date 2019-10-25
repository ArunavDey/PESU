#loginasadmin 
login_id="LIBRARIANPESIT"
password="kdjjjfjbu321"
l_id=input("enter login id:")
passwd=input("enter password:")
while(l_id!=login_id or passwd!=password):
  l_id=input("enter login id:")
  passwd=input("enter password:")
  if(l_id!=login_id or passwd!=password):
    print("invalid username or password")
print("logged in successfully")
