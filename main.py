from PianoProgram.Login import Login
from PianoProgram.Calendar import Calendar
from PianoProgram.Update import Update_information
import os
import time
import sqlite3

#test
def main():
	print("Welcome to PianoProgram")
	Login()
	conn = sqlite3.connect("teaching.db")
	c = conn.cursor()
	Update_information(c, conn)
	time.sleep(1)
	os.system("clear")
	Calendar(c, conn)

if __name__ == '__main__':
	main()