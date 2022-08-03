print(
    "." * 123
)

formatter = "{} {} {} {}"

print(
    formatter.format(1 ,2 ,3 ,4)
)
print(
    formatter.format("one", "two", "three", "four")
)

print(
    formatter.format(True, False, False, True)
)

print(
    formatter.format(formatter, formatter, formatter, formatter)
)

print(
    formatter.format(
        "Your my sun and moon,",
        "Your everything in between,",
        "You make flowers bloom,",
        "I don't know what I did to get lucky like this"
))