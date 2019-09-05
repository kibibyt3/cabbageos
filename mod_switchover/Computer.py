import colors
import sys
import time
import os
from time import sleep
from random import shuffle
from random import choice

class Computer:
	root = False
	username = ""
	password = ""
	hostname = ""
	ip = ""
	files = []
	dirs = []
	crackSecure = False
	regSecure = False
	fileName = ""
	cwd = ""

	def loginScreen(self):
		loop = True
		while loop:
			command = input(colors.LIGHT_BLUE + '> ' + colors.DEFAULT)
			if command == 'register':
				register(self)
			elif command == 'login':
				login(self)
			elif command == 'help':
				help(self)
			elif command == 'exit':
				exit(self)
			else:
				print("Input misunderstood. Type 'help' to see possible commands.")

	def addUser(un, pw):
		
