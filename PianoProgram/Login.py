import os
import time

def Login():
	while True:
		username = input("Please enter your username: ")
		password = input("Please enter your password: ")
		if username == "admin" and password == "admin":
			print("Login successful")
			break
		else:
			print("Login failed, please try again!\n")
		time.sleep(2)
		os.system('clear')