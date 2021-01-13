#!/usr/bin/python3

import os
import sys
import time
import random


# global variables
sureness = 0.0
similar_num = 0
# global functions
def get_similar(result_array):
	x = 0
	global sureness
	global similar_num
	for element in range(0, len(result_array)):
		if (x+1 < len(result_array)):
			if (result_array[x] >= result_array[x+1]):
				int_distance = result_array[x] - result_array[x+1]
				if (int_distance <= 0.25):
					sureness += 1.0/(len(result_array)-1)
					#print (str(sureness))
					similar_num = result_array[x]


				else:
					sureness = sureness - 1.0/(len(result_array)-1)
					similar_num = result_array[x] + (result_array[x] - result_array[x+1])
			else:
				int_distance = result_array[x+1] - result_array[x]
				if (int_distance <= 1.0):
					sureness = sureness + 1.0/(len(result_array)-1)
					similar_num = result_array[x+1]
				else:
					sureness = sureness - 1.0/(len(result_array)-1)
					similar_num = result_array[x+1] + (result_array[x+1] - result_array[x])
		x += 1



# main function
def main():
	# define num array
	num_array_input = input("Enter a valid array: ")
	num_array_input = num_array_input.split(",")
	num_array = []
	for element in num_array_input:
		num_array.append(int(element.strip()))
	print ("Input array: " + str(num_array))
	num_result_array = []

	surness = 0.0

	x = 0
	for num in num_array:
		if (x+1 < len(num_array)):
			num_result_array.append(num_array[x] - num_array[x+1])
		else:
			get_similar(num_result_array)
			num_array.append(num_array[x] - int(similar_num))
			break
		x += 1
	print ("\n\n-----------------------")
	print ("Number: " + str(similar_num))
	print ("Sure-ness: " + str(sureness))
	print ("Predicted array: " + str(num_array))
	print ("-----------------------")

# when the program starts
if __name__ == "__main__":
	main()
