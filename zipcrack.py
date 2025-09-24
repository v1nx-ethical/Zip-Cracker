import os

def hash():
	os.system(f"sudo zip2john {filename} > pass.txt")
def cracker():
	os.system("john pass.txt")
def help():
	print("1. Hash")
	print("2. Cracker")
	print("3. Quit")
	
filename = input("Enter A Zip File Path Here: ")
help()

while True:
	command = input("Enter A Option From Above Here ")
	if command == "1":
		print(f"Hashing {filename}...")
		hash()
	if command == "2":
		print(f"Cracking {filename}...")
		cracker()
	if command == "3":
		print("Goodbye!")
		break
		
