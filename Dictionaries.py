colors = {
    "R": "Red",
    "G": "Green",
    "B": "Blue"
}

print(colors.get("B"))
print(colors.get("C", "default"))

orange = colors.get("O")
print("orange: " + str(orange))

print(colors.keys())
print(colors.values())

print(colors.items())
