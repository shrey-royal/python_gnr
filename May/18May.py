# How to unpack a tuple

dog = ("labradog", "doberman", "golder retriever", "german shepherd", "Bulldog", "Husky", "rottweiler")

# dog_1, dog_2, dog_3, dog_4, dog_5, dog_6, dog_7 = dog

# print(dog_1)
# print(dog_2)
# print(dog_3)
# print(dog_4)
# print(dog_5)
# print(dog_6)
# print(dog_7)

# Indexing in tuple

# dog[index_value]

# print(dog[2])

# negative indexing

# print(dog[-7])  # here -1 means the last index's value will be printed

# changing the tuple

# approach1 -: convert the tuple into the list than again after chnaging the list convert it back to tuple

# dog[2] = "abcd"

# approach2 -: type cast the tuple to change something

# myList = list(dog)

# print(myList.insert(2, "abcd"))

# dog = tuple(myList)

# print(dog)

# approach3 -: using for loop to iterate over the tuple

# myList = []

# for x in dog:
#     myList.append(x)

# print(myList)

# Membership operators -: In, not in

apple = ('a', 'p', 'p', 'l', 'e')
fruit = ('a', 's', 'f')
# myList = [(2, 5), (9, 4), (9, 0), (1, 4), (1, 5)]

# print('p' in apple)
# print('d' not in apple)

# for i in (45, 23, 89, 56, 43):
#     print(i, end='\t')

# methods in tuple
print(apple.count('p')) # return the first occurence
print(apple.index('l'))

print(apple * 4)

myTuple = apple + dog

print(myTuple)

'''
why use tuple over list

1. 
tuple - different data type
mix = (1, 'a', 2.3, "royal")
list - similar data type
number = [1, 2.3]
alphabets = ['a', "bcd"]

2. as tuples are immutable, iteration over the tuple is faster compare to list

3. as tuples are immutable, the data will be automatically write-protected

Tasks in tuple -: 

1. Python program to find the size of a tuple
2. Python program for adding a Tuple to List and Vice-Versa
3. Python program to find the maximum and minimum K elements in a tuple
4. Python program to create a list of tuples from given list having number and its cube in each tuple
5. Python program to remove all tuples of length K
6. Python program to extract digits from tuple list
7. Python program to find all pairs combination of two tuples
8. Python program to join tuples if similar initial element
9. Python program to sort a list of tuples by second item
10. Python program to sort a list of tuples in increasing order by the last element in each tuple
11. Python program to sort tuples by frequency of their absolute difference
12. Python program to remove duplicate tuples irrespective of order
13. Python program to order tuples by list
14. Python program to concatenate maximum tuples
15. Python program to flatten tuple of lists to a tuple


'''