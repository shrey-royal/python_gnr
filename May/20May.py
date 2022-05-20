"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# num1, num2, num3, num4, ..., num10 = numbers

# num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = numbers

num1, num2, *others = numbers   # starred expression

# starred expression will return a list

print(f"first element from the tuple is {num1} and second element from the tuple is {num2} and there are some other elements which are {others}")

*others, num9, num10 = numbers

print(f"second last element from the tuple is {num9} and last element from the tuple is {num10} and there are some other elements which are {others}")

num1, *remaining, num10 = numbers

print(f"first element from the tuple is {num1} and last element from the tuple is {num10} and there are some other elements which are {remaining}")
"""

# 1. Python program to assign frequency to tuples

# Input:
# tupList = [(4, 1), (3, 3), (4, 1), (5, 7), (3, 3), (4, 1)]

# Output:
# freqList = [((4, 1), 3), ((3, 3), 2), ((4, 1), 2)]

# from collections import Counter

# tupList = [(4, 1), (3, 3), (4, 1), (5, 7), (3, 3), (4, 1)]
# # unique elements will be ignored(kind of)

# print(f"The list of tuple is {str(tupList)}")

# freqList= [(key, val) for key, val in Counter(tupList).items()]

# print(f"List of tuple with frequency added at the end is {str(freqList)}")

# 2. Python program to sort tuples by total digits

# Unsorted Tuple list : [(43343, 1), (2, 4), (12, 40), (1, 23)]
# Sorted Tuple list : [(2, 4), (1, 23), (12, 40), (43343, 1)]

tupList = [(43343, 1), (2, 4), (12, 40), (1, 23)]

print(f"Unsorted Tuple List is {str(tupList)}")
temp = 0
temp1 = 0

print(len(tupList))

for i in range(len(tupList)):
    temp = len(str(tupList[i])) - 4
    # temp1 = len(str(tupList[i+1])) - 4

    # if temp <= temp1:
    #     myTuple = (tupList[i])