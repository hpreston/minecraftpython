# a favorite sandwich as a Python list
l = [
        "bread",
        "peanut butter",
        "jelly",
        "bread"
    ]

# giving instructions on creation
print("Now is time for {}".format(l[0]))
print("Now is time for {}".format(l[1]))
print("Now is time for {}".format(l[2]))
print("Now is time for {}".format(l[3]))

# simpler way to "loop" through a list
for i in l:
    print("Now is time for {}".format(i))
