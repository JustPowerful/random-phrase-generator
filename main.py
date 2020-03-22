"""
	1 - Change the random generating lists, and rename them in the dictionary
	2 - Specify your input file and output file, and the lists dictionary
	3 - add some text with tags that you want to change randomly
	Example :
	@name@ is @age@ old

	4 - open the output file, you'll get the result
	Warning ---> Keep spaces between tags (input file)
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
		self.tag_list = []

	def generate(self):

		
		# temp files (temp1)
		self.readfile = self.fin.read().replace(" ", "\n")
		tempfile = open("temp.txt", "w")
		tempfile.write(self.readfile)
		tempfile.close()

		readtemp = open("temp.txt", "r")
		temptext = readtemp.readlines()

		# temp files (temp2)
		tempfile2 = open("temp2.txt", "w")

		
		for key in self.gen_dict.keys():
			tag = "@"+key+"@"
			self.tag_list.append(tag)


		for line in temptext:
			res = any(ele in line for ele in self.tag_list) 
			if res:
				TAG = line.replace("@", "").replace("\n", "")
				tempfile2.write(line.replace("@"+TAG+"@", random.choice(self.gen_dict[TAG])))
			else:
				tempfile2.write(line)
		tempfile2.close()
		
		tempfile2 = open("temp2.txt", "r")
		readtemp2 = tempfile2.read()
		self.fout.write(readtemp2.replace("\n", " ")) 
		self.fout.close()

		readtemp.close()
		tempfile2.close()


		os.remove("temp.txt")
		os.remove("temp2.txt")
		



class __name__():
	# the code runs here
	# generation lists
	genre = ["RPG", "FPS", "ADVENTURE", "SURVIVAL", "TYPER", "PUZZLE"]
	character = ["rebel", "soldier", "hacker", "doctor", "car driver", "sword man", "robot", "kid", "assassin", "builder", "farmer", "time traveller", "survivor"]
	enemy = ["corrupted governemnt", "zombies", "viruses", "skeletons", "spiders", "bullies", "monsters", "bats", "snakes", "aliens", "dinosaurs", "witches", "clowns"]
	end = ["bad", "happy"]
	
	# main generation dict
	DICT = {
		"genre": genre,
		"character": character,
		"enemy": enemy,
		"end": end
	}

	GENERATOR("phrase.txt", "generated.txt", DICT).generate()
