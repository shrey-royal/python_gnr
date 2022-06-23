# 5. Python program to remove all tuples of length K

tupleList =  [(1, 4), (9, 4, 2), (4,5,6,8), (2, 6, 8), (3, 0, 1), (4, 4, 1)]
K = 2
print("Initial List : " + str(tupleList))

# removing tuples of length k 
filteredList = [tup for tup in tupleList if len(tup) != K]

# Printing the filtered list 
print("List of tuples after removing tuple of length k : " + str(filteredList))