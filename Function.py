def love(name):
    print("I love " + name)


love("pizza")


def test(age):
    age = input("age:")
    print("age:" + age)


test(12)


def calculation(a, b, c):
    print(a + b + c)
    print(a - b - c)
    print(a * b / c)


calculation(8, 3, 2)


def calculation2(a, b, c):
    return a + b + c


result = calculation2(8, 3, 2)
print("result: " + str(result))
