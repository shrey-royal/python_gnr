# String functions in python
"""
myString = "Royal_Technosoft_pvt._ltd."
# myString = "RGHJM  Bhhh"

# print(len(myString))
print(myString.center(50, "*"))
print(myString.capitalize())
print(myString.casefold())
print(myString.count("o"))
print(myString.count("o", 0, 10))
print(myString.count("o", 0, -1))
myString = "before╰(*°▽°*)╯after"
# print(myString.encode(encoding="ascii", errors="strict")) #it will return us errror
print(myString.encode(encoding="ascii", errors="ignore")) #it will ignore the error
print(myString.encode(encoding="ascii", errors="replace")) #it will replace the error
print(myString.encode(encoding="ascii", errors="xmlcharrefreplace")) #it will give xml refs in place of errors
print(myString.encode(encoding="ascii", errors="backslashreplace")) #it will replace the error
print(myString.encode(encoding="ascii", errors="namereplace")) #it will replace the name in place of error
# myString = "Royal_Technosoft_pvt._ltd."

myString = "Hello\tWorld\tok\tbye."
print(myString.endswith("ltd."))
print(myString.endswith("ltd.", 0, -1))
print(myString.endswith("Tech", 0, 10))
print(myString.expandtabs(2)) # 8 humbak maa

"""
# myString = "Leela Hotel --> {per_dis}"
# print(myString.format(per_dis = 1500))
"""
myString = "Royal_Technosoft_pvt._ltd."
print(myString.find("c"))   # it will return the index of first occurance of c
print(myString.find("o", 0, 2))   # it will return the index of first occurance of o in a range
print(myString.index("c"))   # it will return the index of first occurance of c
print(myString.index("o", 0, -1))   # it will return the index of first occurance of o in a range
"""
myString = "2.3"
# print(myString.isalnum())   # it will return true if all characters are alphanumeric (alphabet or numbers)
# print(myString.isalpha())   # it will return true if all characters are alphabetic (a-z or A-Z)
# print(myString.isdecimal())   # it will return true if all characters are decimal (0-9)
# print(myString.isdigit())   # it will return true if all characters are digits (0-9) (Whole numbers)
print(myString.isidentifier())   # it will return true if all characters are valid identifier characters (alphanumeric or _)
print(myString.islower())   # it will return true if all characters are lowercase (a-z)
print(myString.isnumeric())   # it will return true if all characters are numeric (0-9)
print(myString.isprintable())   # it will return true if all characters are printable (alphanumeric or _)
print(myString)