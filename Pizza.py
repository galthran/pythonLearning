class Pizza:

    def __init__(self, name, prize, size):
        self.name = name
        self.prize = prize
        self.size = size

    def toString(self):
        print("Pizza {name: " + self.name + " ,prize: " + str(self.prize) + " , size: " + self.size + "}")

