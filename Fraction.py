class Fraction:

    def __init__(self, nr, dr=1):
        self._nr = nr
        self._dr = dr
        if self._dr < 0:
            self._nr *= -1
            self._dr *= -1

    def show(self):
        print(f'{self._nr}/{self._dr}')

    @property
    def nr(self):
        return self._nr

    @property
    def dr(self):
        return self._dr

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self._nr * other._nr, self._dr * other._dr)

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self._nr * other._dr + other._nr * self._dr, self._dr * other._dr)

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


# if __name__ == '__main__':
#     f1 = Fraction(2, 3)
#     f1.show()
#     f2 = Fraction(2, -3)
#     f2.show()
#     f3 = Fraction(-5, -6)
#     f3.show()
#     print(Fraction.hcf(5, 8))
#
#     result = f1.add(3)
#     print(result.show())
#     print("---------")

