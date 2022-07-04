'''
random_list = ["string", ['w', 'w', 'e'], "wwe"]
# List Comprehension - > iterate


# print(len(random_list))

for i in range(0, len(random_list)):
    for j in random_list[i]:
        print(j)

'''


# Matrices - nested lists

# random_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
# print the matrice
for i in range(0, len(random_list)):
    for j in random_list[i]:
        print(j, end=" ")
    print()

'''
'''
# print the position of every element in the matrice
print()
for i in range(len(random_list)):
    for j in range(len(random_list)):
        # print(i, j, sep=", ", end=" ")
        print(f"({i}, {j})", sep=", ", end=" ")
    print()

'''

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# c = a+b

# print(c)

random_list = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0], 
]

temp_list = []

n = 3
m = 2 

temp_list = [0] * n

for i in range(n):
    temp_list[i] = [0] * m

print(temp_list)


# for i in range(len(a)):
#     for j in range(len(b[i])):
#         random_list[i][j] = a[i][j] + b[i][j]

# print(random_list)
