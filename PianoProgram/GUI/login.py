import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class Login(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		

if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = Login()
	form.show()
	sys.exit(app.exec())





