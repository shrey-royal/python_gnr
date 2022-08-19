# File Handling
# File handling is the process of reading and writing data to a file.
# we have 4 modes of file handling
# r - read mode - open a file for reading only, return error if file does not exist
# w - write mode - create a new file and write data to it
# a - append mode - add data to the end of the file
# x - create a specific file and returns error if the file already exists

# file will be handled in text (t) or binary mode (b)
'''
# Open a file
# open() - open a file

# file = open("test.txt", "w")    # creates a file if it does not exist

# file.write("We are Royalites and We are learning Python.")      # write data to the file

# file.close()    # close the file


# print(file.read())

# creating and writing to a file
f = open("name.txt", "w")

f.write("Your name is " + input("Enter your name: "))

f.close()

# reading from a file
f = open("name.txt", "r")

print(f.read())

f.close()

f = open("name.txt", "a")

f.write("\nYour name is " + input("Enter your name: "))

f.close()
'''
# string encoding


# f = open("demo.txt", "x")   # creates a file if it does not exist

# delete a file
# import os

# os.remove("demo.txt")



'''
Programs on File Handling

1. Create a file and ask user for a name and write it to the file and read data from the file.

2. Create 2 files called (even.txt, odd.txt) and ask user for a range of number after that store even numbers in 1st file and odd numbers in 2nd file.

3. Create a file if the file is already exists then append data(user enetered strings in new line) to the file.

4. Create a file that checks if the specified file name is exists or not. (user will enter the file name, print custom message)

5. create a file called palindrome and ask user to enter a string and check if the string is palindrome or not.

6. ask user for a file name and if exists then if file found then ask user for it's confirmation then delete the file. (Yes/No)

7. Ask user for a number and scan a string, store that strings in a list, check every string if that string have vowels in it or not, if vowels are present than store that string in a new file called with vowels.txt else store that string in a new file called without consonants.txt

8. same as above but here take 3 files (vowels, consonants, symbols) and store the data in those files.

9. ask user for a range of numbers and stores those numbers in a file. after that read numbers from that file and if that number is a perfect number then make a list of that nunmbers and again store it in the another file called perfect number. and print them.

6 = 1, 2, 3 (add, mul should be equal to 6)

'''