import os
from datetime import date
	
def Add_student(c, conn):
	student_name = input("What is the student's name?\n")
	lesson_day = input("On what days do you teach this student(e.g. Mon)?\n")
	lesson_time = input("At what time do you teach this student?\n")
	lesson_length = input("How long is each lesson?\n")
	lesson_price = input("How much are you charging each lesson?\n")
	os.system("clear")
	user_response = input("Are you sure you are satisfied with all the entries(y/n)?\nname = %s\nday = %s\ntime = %s\nlength = %s\nprice = %s\n" % (student_name, lesson_day, lesson_time, lesson_length, lesson_price))
	if user_response.lower() == "y":
		today = date.today()
		print("Adding student to database")
		c.execute("INSERT INTO calendar VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (student_name, lesson_day, lesson_time, lesson_length, lesson_price, 0, 0, today))
		conn.commit()
		#Add student to database
	elif user_response.lower() == "n":
		os.system("clear")
		Add_student()