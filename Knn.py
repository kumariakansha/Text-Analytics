
import csv
import random
import math
import operator
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open('C:/Users/akank/Downloads/iris.csv', 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
   trainingSet=[]
   testSet=[]
   split = 0.2
   loadDataset('iris.csv', split, trainingSet, testSet)
   print('Train set: ' + repr(len(trainingSet)))
   print('Test set: ' + repr(len(testSet)))
	# generate predictions
   predictions=[]
   k =1
   k_range= []
   k_scores = []
   for l in range(1,20):
       
       for x in range(len(testSet)):
           neighbors = getNeighbors(trainingSet, testSet[x], l)
           result = getResponse(neighbors)
           predictions.append(result)
           
    
       accuracy = getAccuracy(testSet, predictions)
       print('Accuracy: ' + repr(accuracy) + '%')
       k_range.append(k)
       k_scores.append(accuracy)
   plt.plot(k_range, k_scores)
   plt.xlabel('Value of K for KNN')
   plt.ylabel('Cross-validated accuracy')
   print(k_range)
   print(k_scores)
   myData = [k_range, k_scores]  
   myFile = open('plottheknn.csv', 'a')  
   with myFile:  
       writer = csv.writer(myFile)
       writer.writerows(myData)

main()

#k_score[0] = 100
 #k_range[0] = 0


# search for an optimal value of K for KNN

# range of k we want to try
#k_range = range(1, 31)
# empty list to store scores
#k_scores = []

# 1. we will loop through reasonable values of k
#for k in k_range:
# 2. run KNeighborsClassifier with k neighbours
   # knn = KNeighborsClassifier(n_neighbors=k)
# 3. obtain cross_val_score for KNeighborsClassifier with k neighbours
#scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
# 4. append mean of scores for k neighbors to k_scores list
#k_scores.append(scores.mean())


#print(k_scores)