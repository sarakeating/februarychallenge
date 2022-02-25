## Filename: main.py
## Program: GDSC February Challenge
## Programmer: Sara Keating
## Date of first version: 01/02/2022
## Description: This program takes an input array and a target sum
##				and returns a quadruple from the array that satisfies
## 				the target sum.


def findQuadruple(inputArray, targetSum, depth=4):
	
	outputArray = []
	prevSum = 0

	for x, item in enumerate(inputArray):
		while depth > 0:
			for i in range(x+1, len(inputArray)):
				if prevSum + inputArray[i] == targetSum:
					outputArray.append([prevSum, inputArray[i]])	
					break
				else:
					prevSum += inputArray[i]
					findQuadruple(inputArray, targetSum, depth - 1)
			break

	return outputArray


# Tests go here
# print(findQuadruple([7,6,4,-1,1,2], 16))
print(findQuadruple([1, 2, 3, 4], 5))
