# Dictionary - Ordered, Mutable and Unique (not allow dupicates) collection of pair containing key and values

# mydict = {key:value}
# mydict = {
#     "name" : "royal",
#     "address" : "Navrangpura",
#     "turnover" : "100 Cr",
#     "another_dict": {
#         "model" : "Model_name"
#     },
#     "krutarth" : (21, "single", "1.5 Lac")
# }

# print(mydict)

# Royal Jamanvaar for 1 day

# Employees_Choice = {
#     "Dhiraj Sir" : {"Breakfast" : "Dosa", "Lunch" : "Punjabi", "Dinner" : "Khichdi-Kadhi"},
#     "Niraj Sir" : {"Breakfast" : ["khaman", "jalebi"], "Lunch" : "Kathiyawadi", "Dinner" : "Gujarati"},
#     "Rutvi Ma'am" : {"Breakfast" : "Fruit", "Lunch" : "South Indian", "Dinner" : "Maggie"},
#     "Zafar Sir" : {"Breakfast" : "Ganthiya", "Lunch" : "Gujarati", "Dinner" : "Pulav"},
# }

# print(Employees_Choice, end="\n\n\n")

# print(list(Employees_Choice.keys()))    # return an object of keys
# print(list(Employees_Choice.values()))  # return an object of values only

# name = input("Enter the name: ")

# print(Employees_Choice[name])
# print(Employees_Choice.get(name))
# above both ways are same - returns the value of the specified key

# choice = input("what do you want to see (Breakfast, Lunch or Dinner) ? ")

# print(Employees_Choice[name][choice])

# for x in Employees_Choice[name][choice]:
#     print(x)


# car = {}

# car.setdefault("model")

model = input("Enter model: ")
fuel_type = input("Enter Fuel type: ")
average = input("Enter Average: ")
price = input("Enter Price: ")

car = {
    "model" : model,
    "fuel_type" : fuel_type,
    "average" : average,
    "price" : price
}

Engine_type = input("Enter engine type: ")

car.update({"Engine Type" : Engine_type})
print(car)