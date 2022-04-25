# list
# What is List?
# List is a collection which is ordered and changeable. Allows duplicate members.

# change the value of the list. --> mutable/changeable
# lists are ordered and allows duplicate members.
# syntax-: 
# mylist = ['a', 'b', 'c', 'd']

# characters = ['a', 'b', 'c', 'd']
# numbers = [234, 4565, 35 ,5677]
# names = ['John', 'Mary', "Steve", 'Bob']
# mix_list = ['a', 234, 'b', 'c', 'd', 234, 'e', 'f', "isabella", "Shinchan"]

# print(characters)
# print(numbers)
# print(names)
# print(mix_list)


veg = ['tomato', 'potato', 'carrot', 'onion', 'cucumber']

# print(veg[-1])
# print(max(veg)) # max returns the greatest value of the list
# print(min(veg)) # min returns the smallest value in the list
# print(len(veg)) # length of the list
# print(sorted(veg)) # sort the list

# list2 = veg # list2 is a reference to veg
#here list2 is just a label to veg

# print(list2)

# veg.append('cabbage') # add a new item to the list
# print(list2)
# print(veg)

# list2.append('garlic')
# print(veg)
# print(list2)



# veg.clear() # clear the list
# print(veg)

# print(veg.count('carrot')) # count the number of items in the list
# print(veg)

list3 = veg # list3 is a reference to veg

list4 = veg.copy() # copy the list

# print(list4)

# veg.clear()
# print(list4)

# mix_veg = ['garlic 2.0']
# veg.extend('carrot 2.0') # extend the list

# print(veg)

# print(veg.index('carrot')) # find the index of the item
# veg.reverse() # reverse the list
# print(veg)

# veg.remove('carrot') # remove the item from the list
# print(veg)

# veg.insert(2, 'garlic') # insert the item at the specified index
# print(veg)

veg[2] = 'garlic' # replace the item at the specified index
print(veg)