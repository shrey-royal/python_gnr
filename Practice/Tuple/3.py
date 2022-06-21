# 3. Python program to find the maximum and minimum K elements in a tuple

numbers = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10)
k = int(input("Enter k: "))

sortedList = sorted(list(numbers))
min_element = []
max_element = []

# finding minimum elements
for i in range(k):
    min_element.append(sortedList[i])

for i in range(len(sortedList) - k, len(sortedList)):
    max_element.append(sortedList[i])

print(min_element, max_element, sep="\n")