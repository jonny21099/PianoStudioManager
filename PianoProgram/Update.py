import os 
from datetime import date

def Update_information(c, conn):
	today = date.today()
	c.execute("SELECT last_updated FROM calendar")
	result = c.fetchall()
	print(result[0][0])
	if result[0][0] < str(today):
		#if last update is before today then reupdate
		
	else:
		print("This is the latest update")
	
