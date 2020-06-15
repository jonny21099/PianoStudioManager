import os

def View_unpaid(c, conn):
	c.execute("SELECT student_name, lesson_length, lesson_price, total_lessons, total_price, last_updated FROM calendar WHERE total_lessons = 0")
	result = c.fetchall()
	if result == []:
		print("All lessons have been paid")
	else:
		print("|{:12}|{:13}|{:12}|{:13}|{:11}|{:12}|".format("Student Name", "Lesson Length", "Lesson Price", "Total Lessons", "Total Price", "Last Updated"))
		print(" ------------ ------------- ------------ ------------- ----------- ------------")
		for each in result:
			print("|{:^12}|{:^13}|{:^12}|{:^13}|{:^11}|{:^12}|".format(each[0], str(each[1]) + " minutes", "$" + str(each[2]) + " hourly", str(each[3]) + " lessons", "$" + str(each[4]), each[5]))
		