"""
	This script supports one tag on every line
	Example :
	@name@ is the best student in his university
	arnold aged @age@
	etc...
"""

import random
import os

class GENERATOR():

	def __init__(self, input_file, output_file, gen_dict):
		
		if (os.path.exists(output_file)):
			os.remove(output_file)

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
	genre = ["RPG", "FPS", "ADVENTURE", "SURVIVAL", "TYPER", "PUZZLE"]
	character = ["rebel", "soldier", "hacker", "doctor", "car driver", "sword man", "robot", "kid", "assassin", "builder", "farmer", "time traveller"]
	enemy = ["corrupted governemnt", "zombies", "viruses", "skeletons", "spiders", "bullies", "monsters"]
	
	# main generation dict
	DICT = {
		"genre": genre,
		"character": character,
		"enemy": enemy
	}

	GENERATOR("phrase.txt", "generated.txt", DICT).generate()
