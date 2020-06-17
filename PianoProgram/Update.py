import os 
from datetime import date
from datetime import datetime
from datetime import timedelta

def Update_information(c, conn):
	today = date.today()
	c.execute("SELECT student_name, lesson_day, lesson_price, last_updated FROM calendar")
	result = c.fetchall()
	if result[0][3] < str(today):
		#Update everyone
		for index in range(len(result)):
			last_updated_weekday = datetime.strptime(result[index][3], "%Y-%m-%d").weekday()
			#This completes the scenario if  the last updated day of the week is less than the lesson
			#These conditions align moves the last_updated day forward so that it's the same as the lesson day
			if last_updated_weekday < int(result[index][1]):
				difference = int(result[index][1]) - last_updated_weekday
				new_last_updated = datetime.strptime(result[index][3], "%Y-%m-%d") + timedelta(days=difference)
				if new_last_updated.date() <= today:
					c.execute("UPDATE calendar set last_updated = ?, total_lessons = total_lessons + 1, total_price = total_price + ? WHERE student_name = ?", (new_last_updated.date(), result[index][2], result[index][0]))
					conn.commit()
				else: 
					c.execute("UPDATE calendar set last_updated = ? WHERE student_name = ?", (today, result[index][0]))
					conn.commit()
	else:
		print("This is the latest update")







	# for each in range(len(result)):
	# 	if result[each][0] < str(today):
	# 		#if last update is before today then reupdate
	# 		new_last_updated = datetime.strptime(result[each][0], "%Y-%m-%d")
	# 		last_updated_day = new_last_updated.weekday()
	# 		new_lesson_day = int(result[each][1])
	# 		price = result[each][3]
	# 		name = result[each][2]
	# 		if last_updated_day < new_lesson_day:
	# 			difference = new_lesson_day - last_updated_day
	# 			new_last_updated += timedelta(days=difference)
	# 			c.execute("UPDATE calendar set last_updated = new_last_updated, total_lessons = total_lessons + 1, total_price = total_price + price WHERE student_name = name")

		
	# else:
	# 	print("This is the latest update")
	
