myString = "Royal Technosoft pvt. Ltd."

"""
print(myString.ljust(30, '*'))  # Left Justified
print(myString.lstrip(' '))  # Remove Left Spaces
print(myString.partition('.'))  # Partition it returns string in tuple
print(myString.replace('R', 'dp_r'))  # Replace
print(myString.removeprefix('R'))  # Remove Prefix
print(myString.removesuffix('Ltd.'))  # Remove Suffix
"""

print(myString.rfind('o'))  # Right Find
print(myString.rsplit('o'))  # Right Split, it returns string in set
print(myString.splitlines())  # Split Lines
print(myString.startswith('r'))  # Start With
print(myString.swapcase())  # Swap Case
print(myString.title())  # Title
print(myString.upper())  # Upper
print(myString.zfill(40))  # Zfill