import os 
import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import numpy as np

def Update_information(c, conn):
	print("Updating... Please wait")
	time.sleep(3)
	today = date.today()
	c.execute("SELECT student_name, lesson_day, lesson_price, last_updated FROM calendar")
	result = c.fetchall()
	if result[0][3] < str(today):
		#Update everyone
		for index in range(len(result)):
			number_of_weekdays = int(np.busday_count(result[index][3], str(today), weekmask = result[index][1]))
			c.execute("UPDATE calendar SET last_updated = ?, total_lessons = total_lessons + ?, total_price = total_price + (? * ?) WHERE student_name = ?", (today, number_of_weekdays, number_of_weekdays, result[index][2], result[index][0]))
			conn.commit()
