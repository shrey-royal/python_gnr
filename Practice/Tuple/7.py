'''
7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

'''

# Creating Tuples and printing values
tuple1 = (1, 4)
tuple2 = (3, 9)
print("First tuple : " + str(tuple1))
print("Second tuple : " + str(tuple2))

# finding all pair Combination of tuples 
pairCombi = [] 
for val1 in tuple1:
    for val2 in tuple2:
        tup = [val1, val2]
        pairCombi.append(tuple(tup))

for val1 in tuple2:
    for val2 in tuple1:
        tup = [val1, val2]
        pairCombi.append(tuple(tup))

# Printing tuple Combination 
print("All pair Combinations are  : " + str(pairCombi))
