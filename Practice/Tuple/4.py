# 4. Python program to create a list of tuples from given list having number and its cube in each tuple

numbers = [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]
myList = []

for j in range(len(numbers)):
    for i in numbers[j]:
        myList.append(i)

myList.sort()
print(myList)