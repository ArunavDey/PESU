members = {"lol what":[["11","11","1111"],["11","11","11"]]}
def newreg():
    name = input("\nEnter Full name: ")
    dob = input("Enter Date of Birth (DD/MM/YYYY): ").split("/")
    date = input("Enter Date of Registration (DD/MM/YYYY): ").split("/")
    l = []
    l.append(dob)
    l.append(date)
    members[name] = l
    print("Registration successful!\n")


def mem():
    c = 1
    for i in members:
        print(f"\n{c}. {i} | DOB: {members[i][0]} | Reg. Date: {members[i][1]}\n")
c = True
while c is True:
    opt1 = int(input("1.Register new Members\n2.View Members\n3.Log out\n"))
    if opt1 == 1:
        newreg()
    elif opt1 == 2:
        mem()
    elif opt1 == 3:
        print("\nLogged out")
        c = False
    else:
        while opt1 != 1 or opt1 != 2 or opt1 != 3:
            print("Invalid option, try again.")
            opt1 = int(input("\n1.Register new Members\n2.View Members\n3.Log out\n"))
