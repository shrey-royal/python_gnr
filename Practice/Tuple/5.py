# 5. Python program to remove all tuples of length K

myList = [(1, 23, 45, 56), (5, 2, 67, 78, 23), (2, 4), (54, 2), (23, 67, 34, 35)]
k = int(input("Enter k: "))
remove = []

for j in range(len(myList)):
    count = 0
    for i in myList[j]:
        count += 1
    # print(count)
    if count == k:
        remove.append(j)
    
print(remove)