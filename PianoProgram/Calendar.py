import os
import sys
import time
from PianoProgram.Add_student import Add_student
from PianoProgram.View_unpaid import View_unpaid
from PianoProgram.Update import Update_information

def Calendar(c, conn):
	user_option = input("What would you like to do?\n1.View all unpaid lessons\n2.Add new student\n3.Quit\n")
	#View all unpaid lessons
	if user_option == "1":
		time.sleep(0.5)
		os.system("clear")
		View_unpaid(c, conn)

	#Add new students
	elif user_option == "2":
		time.sleep(0.5)
		os.system("clear")
		Add_student(c, conn)
		time.sleep(0.5)
		os.system("clear")

	#quit
	elif user_option == "3":
		sys.exit(0)

	#Invalid entry
	else:
		print("\nPlease enter a valid input")
		time.sleep(1)
		os.system("clear")
	
	Calendar(c, conn)
