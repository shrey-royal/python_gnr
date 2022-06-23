'''
15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)

'''

# creating the tuple of list and printing values
listTup = ([4, 9, 1], [5 ,6])
print("The tuple of list : " + str(listTup))

# flattening of tuple of list 
flatTup = tuple(sum(listTup, []))

# Printing the flattened tuple 
print("Tuple after flattening : " + str(flatTup))
