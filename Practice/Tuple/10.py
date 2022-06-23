'''
10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

'''

# Python program to sort a list of tuples in 
# increasing order by the last element in each tuple

# Creating and Print list 
tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]
print("List of Tuple before sorting : " + str(tupList))

# Sorting List of Tuples in Increasing order by last element 
listLen = len(tupList); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(tupList[j][-1] > tupList[j + 1][-1]):
            swap = tupList[j]
            tupList[j] = tupList[j + 1]
            tupList[j + 1] = swap

#Printing Sorted List 
print("List of Tuple after sorting : " + str(tupList))
