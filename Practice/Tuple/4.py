# 4. Python program to create a list of tuples from given list having number and its cube in each tuple

myList = [6, 2, 5 ,1, 4]

# Creating list of tuples 
tupleList = [(val, (val*val*val)) for val in myList] 
'''
for val in myList:
    myTuple = (val, (val*val*val))
    tupleList.append(myTuple)
'''

# print the result
print("The list of Tuples is " , tupleList)