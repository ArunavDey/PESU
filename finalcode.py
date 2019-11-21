import csv
import pandas as pd
import pathlib as pl
import time
import sys
from simplecrypt import encrpt, decrpyt 
from getpass import getpass
book=[['Advanced Engineering Mathematics','Erwin Kreyzig','maths','420'],['Higher Engineering Mathematics','BS Grewal','maths','69'],['Higher Engineering Mathematics','BV Ramana','maths','420'],['Calculus','James Stewart','maths','69'],['How to solve it by computer','RG Dromey','CSE','69'],['The C puzzle book','Alan R Feuer','CSE','420'],['The C Programming Language','Brian Kernighan and Dennis Ritchie','CSE','420'],['Expert C Programing','Peter van der Linden','CSE','69'],['Engineering Chemisry','Gadag and Nityananda shetty A','chem','420'],['Fundementals of molecular spectroscopy','Banwell','chem','69'],['Engineering Chemistry','PC jain and Monica jain','chem','420'],['Engineering Chemistry','wiley publication','chem','420'],['Industrial Electrochemistry','Pletcher and Walsh FC','chem','69'],['Atkins Physical Chemistry','Atkins and de Paula','chem','69'],['Electronic devices and circuit theory','robert L Boylestad and Louis Nashelsky','ECE','69'],['Digital Design with an Introduction to Verilog HDL','Morris Moano','ECE','420'],['Electronic Communication Systems,Fundamentals through Advanced','Wayne Tomasi','ECE','420'],['Introduction to Embedded Systems','KV Shibu','ECE','420'],['ARM System Develper Guide','Andrew N Sloss','ECE','69'],['Quantum Physics of Atmos Nuclei and Molecules','Eisberg and Robert','phy','420'],['Quantum Physics','Gasiorowicz','phy','420'],['Principles of Quantum Mechanics','Sankar','phy','69'],['Lectures of Physics','Feynman,leighton and Sands','phy','420'],['Concepts of Modern Physics','Arthur','phy','69'],['Mechanics of Materials','Ferdinand Beer','mes','420'],['Elements of Mechanical Engineering','KR Gopalkrishna','mes','69'],['An Introduction to Mechanical Engineering','Michael Clifford','mes','420'],['Mechatronics:a multidisciplinary approach','W Bolton','mes','69'],['Elements of Manufacturing Processes','BS Nagendra Parashar and RK.Mittal','mes','70'],['Basic Mechanical Engineering','Pravin Kumar','mes','80'],['Basis Electrical Engineering','DC Kulshreshta','EEE','80'],['Basis Electrical Engineering','VN and Arvind Mittle','EEE','87'],['Electrical and Electronic Technology','Hughes,Brown &Smith','EEE','96']]
with open("books.csv", "w+", newline = '') as f:
    writer = csv.writer(f, quoting = csv.QUOTE_MINIMAL)
    writer.writerow(['Book', 'Author', 'Subject', 'Stock'])
    for i in book:
        writer.writerow(i)
books2 = pd.read_csv("books.csv")
path = pl.Path("stinfo.csv")
if path.exists() == False:
    with open("stinfo.csv", "w+", newline = '') as f:
        writer = csv.writer(f, quoting = csv.QUOTE_MINIMAL)
        writer.writerow(['Name', 'DOB', 'Registration', 'Password', 'Lent', 'Fines'])
        writer.writerow(['PESUAdmin', '01/01/2001', '01/01/2019' , 'admin123', '0', '0.0'])
mems = pd.read_csv("stinfo.csv")
def login():
    stinfo = pd.read_csv("stinfo.csv")
    passwd = list(stinfo["Password"])
    lid = ""
    pwd = ""
    uid = list(stinfo["Name"])
    pw = False
    while pw == False:
        lid = input("\nEnter your login ID: ")
        if lid in uid:
            pwd = input("\nEnter the password: ")
            if pwd == passwd[uid.index(lid)]:
                pw = True
            else:
                print("\nInvalid username or password.\n")
        else:
            print("\nInvalid username or password.\n")
    print("\nLogged in.\n")
    def newreg():
        name = input("\nType 2 to go back, else\nEnter full name: ")
        if name.strip() == "2":
            intro()
        else:
            dob = input("\nEnter Date of Birth (DD/MM/YYYY): ").split("/")
            date = input("\nEnter Date of Registration (DD/MM/YYYY): ").split("/")
            adm = input("\nAdmin Permissions [Y/N]: ")
            adm = adm.upper()
            l = []
            l.append(name)
            l.append("/".join(dob))
            l.append("/".join(date))
            if adm == "Y":
                pw = input("\nEnter a pass: ")
                pw1 = input("\nRe-enter the pass to confirm: ")
                while pw1 != pw:
                    print("\nPasswords do not match, try again\n")
                    pw1 = input("\nRe-enter the pass to confirm: ")
                l.append(pw)
            elif adm == "N":
                l.append("")
            else:
                while adm!= "Y" and adm!="N":
                    print("\nInvalid option, try again\n")
                    adm = input("\nAdmin Permissions [Y/N]: ")
                    adm = adm.upper()
            l.append("0")
            l.append("0.0")
            with open("stinfo.csv", "a+", newline = '') as f:
                writer = csv.writer(f, quoting = csv.QUOTE_MINIMAL)
                writer.writerow(l)
            print("\nRegistration successful!\n")
    def mem():
        print(mems.iloc[:,[0,1,2,4,5]])
        #print((pd.read_csv("stinfo.csv")).iloc[:,[0,1,2,4,5]])
        opt = int(input("\n1.Lend books\n2.Go back\n"))
        while opt not in [1,2]:
            print("\nInvalid option. Try again\n")
            opt = int(input("\n1.Lend books\n2.Go back\n"))
        if opt == 1:
            opt1 = int(input("\nSelect user using index: "))
            print(books2)
            bk = int(input("\nSelect book using index: "))
            #(pd.DataFrame(list(pd.read_csv("books.csv")))).at[bk, 'Stock'] -= 1
            #(pd.DataFrame(list(pd.read_csv("stinfo.csv")))).at[opt1, 'Lent'] +=1
            #(pd.read_csv("books.csv")).set_value(bk, 'Stock', (pd.read_csv("books.csv")).iloc[bk, 3]-1) 
            #(pd.read_csv("stinfo.csv")).set_value(opt1, 'Lent', (pd.read_csv("stinfo.csv")).iloc[bk, 4]+1)
            books2.iloc[bk, 3]-=1
            mems.iloc[opt1, 4]+=1
            print("Book lent.")
        elif opt == 2:
            intro()
    def intro():
        c = True
        while c is True:
            opt1 = int(input("\n1.Register new Members\n2.View Members\n3.View Books\n4.Log out\n"))
            if opt1 == 1:
                newreg()
            elif opt1 == 2:
                mem()
            elif opt1 == 4:
                print("\nLogged out\n")
                sys.exit()
            elif opt1 == 3:
                print(books2)
                #print((pd.read_csv("books.csv")))
            else:
                while opt1 != 1 or opt1 != 2 or opt1 != 3:
                    print("Invalid option, try again.")
                    opt1 = int(input("\n1.Register new Members\n2.View Members\n3.View Books\n4.Log out\n"))
    intro()
login()
