#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------
__author__ = "Jose Becerril"
__copyright__ = "Copyright 2018, ST Project"
__credits__ = ["Jose Becerril"]
__license__ = "GPL 2"
__version__ = "1.0.1"
__maintainer__ = "JLBS"
__email__ = "ingjoseluisbecerril@gmail.com"
__status__ = "Debbug"
__execution__ = "python code2.py"
#---------------------------
import random
#---------------------------
class myFirstClass():
	""" Docstring for class"""

	def __init__(self):
		self.list1=[1,2,3,4,5,6,7,8,9,10]
		self.list2=[]
		self.a=5
		self.b=random.randint(1,10)

	def funct1(self):
		if(self.a==self.b):
			print(self.b)
			print("I´M A WINNER")
		else:
			print(self.b)
			print("I´M A LOSSER")

	def funct2(self):
		for i in self.list1:
			self.list2.append(i)
			print(i)
		print(len(self.list1))
		print(len(self.list2))


		random.shuffle(self.list2)
		if(self.list2[5]==6):
			print("Correct")
		else:
			print("Fail")


#---------------------------
#Execution
if __name__ == "__main__":
	t=myFirstClass()
	t.funct1()
	t.funct2()

#---------------------------