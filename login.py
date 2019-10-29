#loginasadmin 
login_id="PESUAdmin"
password="admin123"
l_id=""
passwd=""
while(l_id!=login_id or passwd!=password):
    l_id=input("Enter login ID:")
    passwd=input("Enter password:")
    if(l_id!=login_id or passwd!=password):
        print("Invalid username or password.")
print("Logged in\n")
