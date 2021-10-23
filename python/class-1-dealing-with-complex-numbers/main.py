import math


class Complex(complex):

    def __add__(self, value):
        return Complex(complex.__add__(self, value))

    def __sub__(self, value):
        return Complex(complex.__sub__(self, value))

    def __mul__(self, value):
        return Complex(complex.__mul__(self, value))

    def __truediv__(self, value):
        return Complex(complex.__truediv__(self, value))

    def __str__(self):
        return(
            f"{self.real:.2f}{self.imag:+.2f}i"
            if self.imag < 0
            else f"{self.real:.2f}{abs(self.imag):+.2f}i"
        )

    def mod(self):
        return Complex(complex.__abs__(self))

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
