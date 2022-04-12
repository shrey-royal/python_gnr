#slicing of strings

myString = "Niraj_is_a_good_boi"

# print(myString)

# myString = "0123456789......"
# myString = ".........654321"

# print(myString[start:end:step])
print(myString[0:]) # print the whole string
print(myString[:]) # print the whole string
print(myString[0:10]) # print the first 10 characters
print(myString[0:10:2]) # print the first 10 characters with a step of 2, i.e. 0,2,4,6,8
print(myString[0:19:3]) # print the first 17 characters with a step of 3, i.e. 0,3,6,9,12,15,18
print(myString[::-2]) # print the string in reverse
print(myString[::-1]) # print the string in reverse
print(myString[::-3]) # print the string in reverse with a step of 3
print(myString[15:3:-1]) # print the string from the end to the start
print(myString[13:7:-2]) # print the string from the end to the start with a step of 2
print(myString) #slicing doesn't change the original string

