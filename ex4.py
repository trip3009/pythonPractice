print(
    "." * 123
)

cars = 100 #This is also like fillin the blank. 

space_in_a_car = 4.0 #this will substitute the variable with the 4 thats on the left of the equal sign. 

drivers = 30 #"drivers" will be substituted for 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

print(
    "There are", cars, "cars available." #"cars" will be replaced w/ "100".
    )
print(
    "There are only", drivers, "drivers available." #"drivers will be replaced with "4.0".
)
print(
    "There will be", cars_not_driven, "empty cars today."
)
print(
    "We can transport", carpool_capacity, "people today."
)
print(
    "We have", passengers, "to carpool today."
)
print(
    "We need to put about", average_passengers_per_car, "in each car."
)