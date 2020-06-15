import sqlite3
import os
import time
from PianoProgram.Add_student import Add_student


conn = sqlite3.connect("teaching.db")
c = conn.cursor()

def Calendar():
	user_option = input("What would you like to do?\n1.View all unpaid lessons\n2.Update \n3.Add new student\n")
	#View all unpaid lessons
	if user_option == "1":
		print("1")
		# View_unpaid()
	#View all lessons
	elif user_option == "2":
		print("1")
		# Update()
		
	#Add new students
	elif user_option == "3":
		time.sleep(0.5)
		os.system("clear")
		Add_student(c, conn)

	#Invalid entry
	else:
		print("\nPlease enter a valid input")
		time.sleep(1)
		os.system("clear")
		Calendar()


