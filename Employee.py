class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 65:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 65')


if __name__ == '__main__':
    employee = Employee("John", 88)
    employee.age = 47 #88
    employee.display()
