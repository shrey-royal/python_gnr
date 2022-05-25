mySet = {1, 78, 243, "hello", 3.4, "sdfb", 'g'}

numberSet = {1, 78, 34, 89, 23, 90, 89, 234, 546}

# Find the size of a Set in Python

# print(len(mySet))

# Iterate over a set in Python

# for x in mySet:
#     print(x)

# Python – Maximum and Minimum in a Set

# max = mySet[0] # unordered

# max = 0
# min = 1000

# for x in numberSet:
#     if max < x:
#         max = x
#     if min > x:
#         min = x

# print(f"max element of the set is {max}")
# print(f"min element of the set is {min}")

# Python – Remove items from Set

# del numberSet
# print(numberSet)
# numberSet.remove(int(input("Enter any number that you want to remove: ")))
# print(numberSet)


# Python – Check if two sets have at-least one element common

# print(numberSet)
# print(mySet)

# if mySet.intersection(numberSet):
#     print("true")
# else:
#     print("false")


# Python program to find common elements in three lists using sets

# list1 = [1, 23, 45, 6, 89]
# list2 = [8, 7, 6, 4, 3]
# list3 = [67, 45, 78, 3, 7, 6]

# s1 = set(list1)
# s2 = set(list2)
# s3 = set(list3)

# s1 = s1.intersection(s2)
# # print(s1)

# s1.intersection_update(s3)
# print(s1)

# Python – Find missing and additional values in two lists

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [4, 5, 6, 7, 8, 9]

# print("Missing value in list1: ", (set(list2).difference(list1)))
# print("Additional value in list1: ", (set(list1).difference(list2)))


# print("Missing value in list2: ", set(list1).difference(list2))
# print("Additional value in list2: ", set(list2).difference(list1))


# Python program to find the difference between two lists


# Task-:

# Python Set difference to find lost element from a duplicated array
# -> do this program using array only (a-b)

# Python program to count number of vowels using sets in given string
# Concatenated string with uncommon characters in Python
# Python – Program to accept the strings which contains all vowels
# Python – Check if a given string is binary string or not
# Python set to check if string is panagram
# Python Set – Pairs of complete strings in two sets
