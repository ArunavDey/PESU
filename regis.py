import csv
import pathlib
members = {}
def newreg():
	name = input("\nEnter Full name: ")
	dob = input("Enter Date of Birth (DD/MM/YYYY): ").split("/")
	date = input("Enter Date of Registration (DD/MM/YYYY): ").split("/")
	l = []
	l.append(dob)
	l.append(date)
	members[name] = l
	path=pathlib.Path("stinfo.csv")
	if(path.exists()==False):
		with open('stinfo.csv', mode='w') as csv_file:
			fieldnames = ['stu_name', 'dateofbirth', 'dateofreg']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			csv_file.close()
	row=[name,members[name][0],members[name][1]]
	with open('stinfo.csv', 'a') as csv_File:
			fieldnames = ['stu_name', 'dateofbirth', 'dateofreg']
			writer = csv.DictWriter(csv_File,fieldnames=fieldnames)
			writer.writerow({'stu_name':name,'dateofbirth':members[name][0],'dateofreg':members[name][1]})
	csv_File.close()
	print("Registration successful!\n")


def mem():
	c = 1
	members={}
	with open('stinfo.csv','r') as file:
		csv_reader=csv.DictReader(file)
		for row in csv_reader:
			i=row['stu_name']
			members[i]=[row['dateofbirth'],row['dateofreg']]
	#print(members)
	for i in members:
		print(f"\n{c}. {i} | DOB: {members[i][0]} | Reg. Date: {members[i][1]}\n")
		c=c+1						
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


	
