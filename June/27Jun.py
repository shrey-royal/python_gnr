# frozen set - immutable and constants
# when a frozen set is declared then it cannot be changed

"""
# set1 = {1, 23 ,56, 34, 67, 89, 243}

print(name)
# converting this set1 into a frozen set

fs1 = frozenset(set1)

print(type(set1))
print(type(fs1))

print(fs1)


name = frozenset({'R', 'u', 't', 'v', 'i'})


print(name)

list1 = list([12, 45, 67, 89, 0])

num  = frozenset(list1)

print(num)

dixnari = {1:"Rutvi", 2:"Zafar", 3:"Krutarth", 4:"Shrey", 5:"Dhiraj Sir"}

# for i in dixnari.items():
#     print(i)

# for key, value in dixnari.items():
#     print(key, " ", value)

new_dix = frozenset(dixnari.items())

# print(new_dix)

for k, v in new_dix:
    print(k, " ", v)
"""
tp = (1, 1)

print(tp)

'''
# SUMMARY of COLLECTIONS

1. List - Ordered, Mutable & Allow Duplicates

2. Tuple - Ordered, Immutable & Allow Duplicates

3. Set - UnOrdered, Immutable & Unique (Duplicates Not Allowed)
    3.1 - Frozen Sets -> UnOrdered, Immutable, Constant, Unique

4. Dictionary - Ordered, Mutable & Unique(keys), Duplicate Values are Allowed

'''