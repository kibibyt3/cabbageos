import sys
import time
import os
from time import sleep
from random import shuffle
from random import choice
import Tools
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
	activeUser = None	

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
			command = input(Colors.LIGHT_BLUE + '> ' + Colors.DEFAULT)
			if command == 'register':
				self.register()
			elif command == 'login':
				self.login(False)
			elif command == 'help':
				self.help()
			elif command == 'exit':
				self.exit()
			else:
				print("Input misunderstood. Type 'help' to see possible commands.")

	def register(self):
		if not self.regSecure:
			regSequence = Tools.Sequence(['Username: ', 'Password: ', 'Confirm Password: '])
			username, password, confPassword = regSequence.execute()
			if password != confPassword:
				print("Password not the same. Try again.")
			else:
				newUser = User.User(username, password, self.hostname)
				newUser.save()
		else:
			print("Cannot register a new user on this machine.")

	def login(self, crack):
		if not crack:
			loginSequence = Tools.Sequence(["Username: ", "Password: "])
			usernameTry, passwordTry = loginSequence.execute()
			userTry = User.User.load(usernameTry)
			if passwordTry != userTry.password:
				print("Login attempt failed.")
			else:
				self.activeUser = userTry
				self.cliScreen()
	
	def help(self):
		print("login: Allows the user to log in\n\
register: Registers a new user\n\
help: Prints the help dialogue\n\
exit: Exits the VM")	

	def exit(self):
		exit()

	def cliScreen(self):
		loop = True
		print(self.activeUser.username)
		print(self.hostname)
		while loop:
			command = input(Colors.LIGHT_BLUE + "%s@%s" % (self.activeUser.username, self.hostname) + Colors.DEFAULT + "> ")
