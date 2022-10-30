fruits = ["apple", "orange", "pear", "banana", "plum"]

print(fruits)
print(fruits[0])
print(fruits[1])

fruits[3] = "melon"

print(fruits)

print(fruits[2:4])
print(fruits[2:])

print("fruits.size: " + str(len(fruits)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)

#list functions

cars = ["audi", "opel", "tesla", "fiat", "ford", "seat"]
print(cars)

polish_cars = ["syrena", "polonez", "trabant"]

cars.insert(1, "bmw")
print(cars)

cars.insert(len(cars), "toyota")
print(cars)

#cars.clear()
#print(cars)

cars.extend(polish_cars)
print(cars)

print(cars.index("toyota"))

cars.insert(len(cars), "toyota")
print(cars.count("toyota"))

cars.insert(len(cars), "Toyota")
print(cars.count("toyota"))

cars_copy = cars.copy();
print(cars_copy)
