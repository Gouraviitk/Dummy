import numpy as np
import json
import pickle
import math
#### Do not add additional imports ####
## You can add inputs to the functions below and return variables as per your requirement##

def setRandomState():
	## sets random state ##
	np.random.seed(seed = 1234)
	## Do not modify this ##

def generateInput(n,l):
	inputs = np.random.randint(100, size=(n,l))
	return inputs
	

def generateLabels(inputs):
	labels = []
	for i in inputs:
		labels.append(np.argmax(i))
	return labels
#def generateBatch():
	

#def activationFunction():
	

#def computeCost():
	

#def backProp():
	

#def forwardProp():
	

#def buildNetwork():
	

#def trainNetwork():
	

#def testNetwork():

n = 100 #no. of datasets to generate
l = 5   #length of inout layer
inputs = generateInput(n,l)	
labels = generateLabels(inputs)
print(inputs)
print(labels)
if __name__ == "__main__":
	setRandomState()
	
