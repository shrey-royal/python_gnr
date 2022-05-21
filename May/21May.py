'''# set - A set is an unordered collections of items, every element should be unique(no duplicates) and mutable means we can change it.

set is mutable(changeable), unordered(no index), no duplicates allowed
syntax -: 

mySet = {1, 2, 3, ..., n}

'''
# basics of sets

# stores multiple data types
# mySet = {1, 2, 3, "python", 2.3}

# print(mySet)
# print(type(mySet))

# set can't have duplicate
# mySet = {1, 2, 1}
# print(mySet)

# conversion from list to set
# myList = ['veggies', 'snacks', 'biscuits', 'fruits', 'ice-creams', 'chocolates']
# print(set(myList))

# mySet = {1, 2, (3, 4)}
# print(mySet)


#Updating the set
# mySet = {23, 45, 79, 34, 13}
# mySet.update((3, 89)) #upate method doesn't care about the tuple or list it must have something that is iterable.
# print(mySet)

# mySet.add(2)
# print(mySet)

# print(mySet[2]) # we can't access index

# mySet.update([88, 66], {23, 11, 44}, '23')  # string is iterable (collection of characters)
# print(mySet)

# mySet.clear()
# print(mySet) # empity set

# mySet[88] = 45
# print(mySet)

# mySet.remove(8888)
# print(mySet)

# mySet.discard(7988)
# print(mySet)

# dummy_set = {11, 13, 79, 23, 88, 89}
# mySet.difference_update(dummy_set)
# print(mySet)

# new_set = mySet.union(dummy_set)
# print(new_set)

# copied_set = mySet.copy()
# print(mySet)
# print(copied_set)


mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}
# print(mySet.difference(dummy_set))

# print(mySet.intersection(dummy_set))
# print(mySet.pop())

# print(mySet)

# mySet.intersection_update(dummy_set)
# print(mySet)

# print(mySet.isdisjoint(disjoint_set))

# print(mySet.issubset(new_set))
# print(mySet.issuperset(new_set))

# print(mySet.symmetric_difference(new_set))      # (mySet - new_set) U (new_set - mySet)
# print(mySet.difference(new_set))                # mySet - new_set

# mySet.symmetric_difference_update(new_set)
# print(mySet)

# del mySet   # keyword
# print(mySet)