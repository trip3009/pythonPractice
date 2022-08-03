from lib2to3.pgen2 import driver


cars = 100 
space_in_a_car = 4.0
drivers = 30 
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(
    "There are", cars, "cars avilable."
)
print(
    "There are only", drivers, "drivers avilble."
)
print(
    "There will be", cars_not_driven, " emply cars today."
)

print(
     "We can transport", carpool_capacity,  "people today."
)

print(
    "We have", passengers, "to carpool today."
)
print(
    "We need to put about", average_passengers_per_car, "in each car."
)
#------------------------#
print(
    "A\nB\nC"
)

print(
    "A\tB\tC"
)
print(
    "X\tY\tZ"
)