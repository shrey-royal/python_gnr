'''
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(mylist, end="\n\n")

for i in range(0, len(mylist)):
    for j in range(0, len(mylist[i])):
        print(mylist[i][j], end="\t")
    print("\n")
'''

'''
list2 = [0] * 10

# for i in range(0, 10):
#     list2.append(i+1)

print(list2)

'''


row = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

matrix = [0] * row

for i in range(0, row):
    matrix[i] = [0] * cols

print(matrix, end="\n\n")

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end="\t")
    print("\n")

# scanning of matrix
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        matrix[i][j] = int(input(f"Enter matrix[{i}][{j}] = "))
    print("\n")

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end="\t")
    print("\n")

# if (choice == '+')