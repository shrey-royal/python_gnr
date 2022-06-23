'''
9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

'''

# Creating a new tuple 
tupleList = [(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]
print("Unordered list : ", str(tupleList))

# Sorting the list of tuples using second item 
listLen = len(tupleList)
for i in range(0, listLen):
    for j in range(0, (listLen - i - 1)):
        if(tupleList[j][1] > tupleList[j+1][1]):
            temp = tupleList[j]
            tupleList[j] = tupleList[j+1]
            tupleList[j+1] = temp

# Printing sorted list 		
print("Sorted List : ", str(tupleList))
