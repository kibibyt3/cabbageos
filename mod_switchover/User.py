import pickle;

class User:
	username = ""
	password = ""
	hostname = ""
	
	def __init__(self, username=None, password=None, hostname=None):
		self.username = username
		self.password = password
		self.hostname = hostname
	
	def save(self):
		with open("saves/users/" + self.username + ".user", 'wb') as saveFile:
			pickle.dump(self, saveFile)

	def load(tryUsername):
		with open("saves/users/" + tryUsername + ".user", 'rb') as saveFile:
			return pickle.load(saveFile)
