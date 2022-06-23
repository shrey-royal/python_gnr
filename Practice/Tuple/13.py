'''
13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

'''

# creating and printing initial lists
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]

print("The original list is : " + str(tupList))
sortingList = ['l', 'a', 'k', 'e']

print("The sorting list is " + str(sortingList))

# Sorting list of tuple 
Dic = dict(tupList)
sortedTupList = [(key, Dic[key]) for key in sortingList]

# Printing sorted List 
print("The ordered tuple list : " + str(sortedTupList))
