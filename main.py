## Filename: main.py
## Program: GDSC February Challenge
## Programmer: Sara Keating
## Date of first version: 01/02/2022
## Description: This program takes an input array and a target sum
##				and returns a quadruple from the array that satisfies
## 				the target sum.


def findQuadruple(inputArray, targetSum):
	
	outputArray = []


	for x, item in enumerate(inputArray):

		if item > targetSum:
			continue 
		
		# looping over the subseequent items in the array, and
		# seeing if each other item and the current element add
		# to the target sum
		for i in range(x+1, len(inputArray)):
			if item + inputArray[i] == targetSum:
				outputArray.append([item, inputArray[i]])	

	# look into using recursion
	

	return outputArray


# Tests go here
# print(findQuadruple([7,6,4,-1,1,2], 16))
print(findQuadruple([1, 2, 3, 4], 5))
