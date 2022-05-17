'''
What is List?
List is an array that is mutable and ordered

LIST - ordered & Mutable
myList = [values_0, value_1, value_n]
myList[1] = value_1.1   //change at any index 

Tuple - ordered & Immutable
myTuple = (value_0, value_1, value_n)
myTuple[1] = value_1.1  //here it will get the error


Tuples are ordered but immutale
immutable means we can not change any value from the tuple once it is declared
'''

# myTuple = (1, 2, 3, 345, 12, 43, 23)

# print(type(myTuple))

# print(myTuple)
# myTuple.append(2)   #attribute error - no method called append
# print(myTuple)

# myTuple[2] = 90 # type error - doesn't support item assignment
# print(myTuple)

# print(myTuple.count(34))
# print(myTuple.index(3))


# tp = (41,)

# print(type(tp))
# print(tp)

# here is the another way to define a tuple
# Our_Names = "Shrey", "Krutarth Sir", "Anjali Ma'am", "Darshita Ma'am", "Zafar Sir", "Prachi Ma'am", "Sahil Sir", "Setu Ma'am"

# myNumbers = 1, 2, 3, 3, 3, 4, 87, 45, 34, 436

# print(Our_Names)
# print(myNumbers)

# print(sorted(Our_Names))
# print(sorted(myNumbers))

# myTuple = (1, "string...", True, False, 1.23)

# print(myTuple)
# print(Our_Names[2:5])   # slicing is allowed and same as lists

# myTuple = tuple((1, 2, 4, 78, 9, 4567))
# # we used the tuple() method to init the tuple
# print(myTuple)

tuple_in_list = [(1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 4, 6, 3, 2, 7)]
list_in_tuple = ([23, 98, 54, 54, 8, 23, 87], [45, 98, 43, 87, 43, 9])
myTuple = ([1], [2], [3])

# myTuple[0].append(233)
myTuple[0].insert(0, 7)
print(myTuple)

print(tuple_in_list)
print(list_in_tuple)