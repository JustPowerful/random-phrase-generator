"""
	This script supports one tag on every line
	Example :
	@name@ is the best student in his university
	arnold aged @age@
	etc...
"""

import random

class GENERATOR():

	def __init__(self, input_file, output_file, gen_dict):
		
		self.fin = open(input_file, "rt")
		self.fout = open(output_file, "at")
		self.gen_dict = gen_dict

	def generate(self):

		self.readfile = self.fin.readlines()
		for line in self.readfile:
			for gen_dicts in self.gen_dict:
				tag = "@" + gen_dicts + "@"
				if tag in line:
					self.fout.write(line.replace(tag, random.choice(self.gen_dict[gen_dicts])))
class __name__():
	# the code runs here


	# generation lists
	name = ["alex", "ben", "mark", "andy"]
	age = ["18", "10", "12"]
	favorite_games = ["minecraft", "super mario bros", "sonic mania"]
	
	# main generation list
	DICT = {
		"name": name,
		"age": age,
		"favorite_games": favorite_games
	}

	GENERATOR("phrase.txt", "generated.txt", DICT).generate()
