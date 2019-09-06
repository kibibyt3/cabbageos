import sys
import time
import os
from time import sleep
from random import shuffle
from random import choice
import Sequence
import User
import Colors

class Computer:
	root = False
	hostname = ""
	ip = ""
	files = []
	dirs = []
	crackSecure = False
	regSecure = False
	cwd = ""

	def __init__(self, root, hostname, ip, files, dirs, crackSecure, regSecure):
		self.root = root
		self.hostname = hostname
		self.ip = ip
		self.files = files
		self.dirs = dirs
		self.crackSecure = crackSecure
		self.regSecure = regSecure

	def loginScreen(self):
		loop = True
		while loop:
			command = str(input(Colors.LIGHT_BLUE + '> ' + Colors.DEFAULT))
			if command == 'register':
				register()
			elif command == 'login':
				login(False)
			elif command == 'help':
				help()
			elif command == 'exit':
				exit()
			else:
				print("Input misunderstood. Type 'help' to see possible commands.")

	def register(self):
		if not regSecure:
			regSequence = Sequence(['Username: ', 'Password: ', 'Confirm Password: '])
			username, password, confPassowrd = regSequence.execute()
			if password != confPassword:
				print("Password not the same. Try again.")
			else:
				newUser = User(username, password, hostname)
		else:
			print("Cannot register a new user on this machine.")

	def login(self, crack):
		if not crack:
			loginSequence = Sequence(["Username: ", "Password: "])
			usernameTry, passwordTry = loginSequence.execute()
			userTry = User()
			userTry.loadUser(usernameTry)
			if passwordTry != userTry.password:
				print("Login attempt failed.")
			else:
				cliScreen()

	def cliScreen():
		loop = True
		while loop:
			command = input(Colors.LIGHT_BLUE + '> ' + Colors.DEFAULT)
