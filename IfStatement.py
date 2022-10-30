x = 4
y = 5
z = 6

if x == 4:
    print("x = 4")

if x == 4 and y == 5:
    print("x = 4; y = 5")

if x == 4 or y == 5:
    print("x = 4 or y = 5")

if x == 5:
    print("x = 5")
elif x == 4:
    print("x = 4")


a = input("a: ")
if 0 < int(a) < 5:
    print("case1")
elif 5 < int(a) < 10:
    print("case2")
else:
    print("case3")
