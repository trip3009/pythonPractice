types_of_people = 10
x = f"There are {types_of_people} types of people" # this means is a f-string function, which allows the types_of_people & 10 be printed.

binary = "binary" 

do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(
    x
)
print(
    y
)
print(
    f"I said: {x}"
)
print(
    f"I also said: '{y}'"
)

hiliarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(
    joke_evaluation.format (hiliarious)
)
w = "This is the left side of..."
e = "a string with a right side"
print(
    w + e
)