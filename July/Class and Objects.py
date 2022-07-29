# # Creating class -> declaring a class
# class Royal():
#     departments = "Management"
#     dept_1 = "Account"

# # Creating object -> instantiate a class
# obj_of_royal = Royal()

# # print(type(obj_of_royal))

# print(obj_of_royal.departments)
# print(obj_of_royal.dept_1)

# print()

######################################################


# class Car():
#     """Welcome to Royal Automobiles"""
#     car_name = ""
#     car_model = ""
#     car_type = ""
#     color = ""
#     fuel_type = ""
#     gear_type = ""
#     mileage = ""
#     price = ""

# c1 = Car()

# print(c1.__doc__)

# c1.car_name = input("Enter Car Name: ")
# c1.car_model = input("Enter Car Model: ")
# c1.car_type = input("Enter Car Type: ")
# c1.color = input("Enter Color: ")
# c1.fuel_type = input("Enter Fuel type: ")
# c1.gear_type = input("Enter Gear Type: ")
# c1.mileage = input("Enter mileage: ")
# c1.price = input("Enter Price: ")

# print(c1.car_name, c1.car_model, c1.car_type, c1.color, c1.fuel_type, c1.gear_type, c1.mileage, c1.price)


# Gujarati Cuisine -> 10 dishes -> enter price -> print


######################################################

class Car():
    model_name = ""
    odo_meter = ""
    def scan_car(self):
        self.model_name = input("Enter model name of the car: ")
        self.odo_meter = int(input("Enter kms: "))
        self.service_type = input("Enter Service type: ")
        self.time = input("Enter time of service: ")
        self.details = input("Enter name and number of the driver (use / to seperate): ")
    
    def print_car(self):
        print(self.model_name)
        print(self.odo_meter)
        print(self.service_type)
        print(self.time)
        print(self.details)

c = Car()

c.scan_car()
c.print_car()

# self keyword specifies the status of the object