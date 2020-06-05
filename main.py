from PianoProgram.Login import Login
from PianoProgram.Calendar import Calendar
import os
import time

def main():
	print("Welcome to PianoProgram")
	Login()
	time.sleep(1)
	os.system("clear")
	Calendar()

if __name__ == '__main__':
	main()