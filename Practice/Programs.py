"""

'''
1. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
'''

words = {'Right':'Left', 'Up':'Down'}

for k in words.keys():
    print(k, end="\t")

scan_word = input("\nEnter any word: ")

print(words.get(scan_word)) if scan_word in words.keys() else print("Not Present")

"""
'''
2.  Ask user to give name and marks of 10 different students. Store them in dictionary. Print the dictionary at the end.
{"s1":35, "s2":40, "s3":30, "s4":55, "s5":39,......., "s10":79}

3.  Sort the above dictionary according to the marks.
{"s3":30, "s1":35, "s5":39, "s2":40, "s4":55}
'''
'''
1. Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
'''

"""
3.  Sort the above dictionary according to the marks.
{"s3":30, "s1":35, "s5":39, "s2":40, "s4":55}

"""

student = {}
sorted_students = {}

print("Please enter subject_name & marks of 10 students")

for i in range(10):
    sub_name = input(f"enter sub_name {i+1}: ")
    marks = int(input(f"enter marks {i+1}: "))
    student[sub_name] = marks

print(student)

temp = []
for key, value in student.items():
    temp.append(str(value) + "_" + key)
temp.sort()

print(temp)

temp2 = []
for string in temp:
    temp2.append(string.split("_"))

print(temp2)

for x, y in temp2:
    sorted_students[y] = x

print(sorted_students)