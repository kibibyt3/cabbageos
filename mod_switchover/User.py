import pickle;

class User:
	username = ""
	password = ""
	hostname = ""
	
	def __init__(self, username, password, hostname):
		self.username = username
		self.password = password
		self.hostname = hostname

	def saveUser(self):
		with open("saves/users/" + username + ".user", 'w') as saveFile:
			pickle.dump((username, password, hostname), saveFile)

	def loadUser(self, tryUsername):
		with open("saves/users/" + tryUsername + ".user", 'r') as saveFile:
			username, password, hostname = pickle.load(saveFile)
