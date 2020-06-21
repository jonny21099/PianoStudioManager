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
		time.sleep(0.4)
		os.system("clear")
		result = View_unpaid(c, conn)
		if result == "1":
			#Make a payment
			student = input("\nWhich student would you like to update payment information for?\n")
			c.execute("SELECT total_lessons FROM calendar WHERE student_name = ?", (student,))
			database_result = c.fetchall()
			if len(database_result) == 0:
				print("This student doesn't exist.\n")
			elif len(database_result) == 1:
				amount = input("\nHow many lessons have been paid?\n")
				c.execute("UPDATE calendar set total_lessons = total_lessons - ?, total_price = total_price - (lesson_price * ?) WHERE student_name = ?", (amount, amount, student))
				conn.commit()

		elif result == "2":
			#go back
			pass

		elif result == "3":
			#quit
			sys.exit(0)

		time.sleep(0.4)
		os.system("clear")

	#Add new students
	elif user_option == "2":
		time.sleep(0.4)
		os.system("clear")
		Add_student(c, conn)
		time.sleep(0.4)
		os.system("clear")

	#quit
	elif user_option == "3":
		sys.exit(0)

	#Invalid entry
	else:
		print("\nPlease enter a valid input")
		time.sleep(0.4)
		os.system("clear")
	
	Calendar(c, conn)
