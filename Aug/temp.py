print("__name__ is ", __name__)

import Test

print("__name__ is ", Test.__name__)

list2 = []

if __name__ == "__main__":
    print("current python file")
    # list2
else:
    print("file is imported")
    # list2