import sqlite3
import os
import time

conn = sqlite3.connect("teaching.db")
c = conn.cursor()

def Calendar():
	user_option = input("What would you like to do?\n1.View all unpaid lessons\n2.View all lessons\n3.Add new student\n")
	#View all unpaid lessons
	if user_option == "1":
		print("1")
		# View_unpaid()
	#View all lessons
	elif user_option == "2":
		print("1")
		# View_all()
	#Add new students
	elif user_option == "3":
		time.sleep(0.5)
		os.system("clear")
		Add_student()

	#Invalid entry
	else:
		print("\nPlease enter a valid input")
		time.sleep(1)
		os.system("clear")
		Calendar()


# def View_unpaid():
#	#view all unpaid lessons

# def View_all():
# 	#View all lessons 

	
def Add_student():
	student_name = input("What is the student's name?\n")
	lesson_day = input("On what days do you teach this student?\n")
	lesson_time = input("At what time do you teach this student?\n")
	lesson_length = input("How long is each lesson?\n")
	lesson_price = input("How much are you charging each lesson?\n")
	os.system("clear")
	user_response = input("Are you sure you are satisfied with all the entries(y/n)?\nname = %s\nday = %s\ntime = %s\nlength = %s\nprice = %s\n" % (student_name, lesson_day, lesson_time, lesson_length, lesson_price))
	if user_response.lower() == "y":
		print("Adding student to database")
		c.execute("INSERT INTO calendar VALUES (?, ?, ?, ?, ?, ?, ?)", (student_name, lesson_day, lesson_time, lesson_length, lesson_price, 0, 0))
		conn.commit()
		#Add student to database
	elif user_response.lower() == "n":
		os.system("clear")
		Add_student()
