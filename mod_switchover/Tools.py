from random import randint

class Sequence:
	queries = []
	
	def __init__(self, queries):
		self.queries = queries

	def execute(self):
		answers = []
		for elem in self.queries:
			answers.append(input(elem))
		return answers

class Tools:
	def ipGen():
		return "%i.%i.%i.%i" % (randint(0, 256), randint(0, 256), randint(0, 256), randint(0, 256))
