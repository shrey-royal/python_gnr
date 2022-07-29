# class Car():
#     def __init__(self):
#         """this is costructor of car class"""
#         self.name = "XC60"
#         self.fuel = "Petrol"
#         self.price = "8500000"

# c1 = Car()
# c2 = Car()

# print(c1.__init__.__doc__)
# # c1.name = "XC90"
# # c1.fuel = "Petrol"
# # c1.price = "9500000"

# print(c1.__dict__)


# '''
# constructor -> used to initialiaz the values to the class variables

# a special method that automatically invoked when you create object

# '''


class Car():
    airbag = 4
    def __init__(self, name, fuel, price):
        self.name = name
        self.fuel = fuel
        self.price = price

    def print_details(self):
        print("-----------Details-----------")
        print("Name:\t\t", self.name)
        print("Fuel:\t\t", self.fuel)
        print("Price:\t\t", self.price)
        print("Airbags:\t", self.airbag)
        print("-----------------------------")

c1 = Car("XC60", "Petrol", 8500000)
c2 = Car("Bolero", "Diesel", 1200000)
c2.transmission = "manual"

c1.print_details()

c2.print_details()
print(c2.transmission)

# Task -: you have to take a number from the user then scan the car details and print the same