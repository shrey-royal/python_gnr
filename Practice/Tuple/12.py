'''
12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

Output:
[(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

'''

# Creating and printing the list of tuples
tupList = [(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]
print("Initial List of Tuples : " + str(tupList))

# Removing all duplicate tuples from the list
sortedTup = [tuple(sorted(val)) for val in tupList]
tupListWoDup = list(set(sortedTup))

# Printing the list of tuples 
print("List of Tuples after removal of duplicates : " + str(tupListWoDup))