from math import *

class Komplex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return Komplex(self.real + other.real, self.im + other.im)
    
    def __sub__(self, other):
        return Komplex(self.real - other.real, self.im - other.im)
        
    def __neg__(self):
        return Komplex(self.real, -self.im)
    
    def __mul__(self, other):
        return Komplex(self.real * other.real - self.im * other.im, self.real * other.im + self.im * other.real)
    
    def __truediv__(self, other):
        return Komplex((self.real * other.real + self.im * other.im) / (other.real**2 + other.im**2), (self.im * other.real - self.real * other.im) / (other.real**2 + other.im**2))
    
    def __abs__(self):
        return sqrt(self.real**2 + self.im**2)
    
    def arg(self):
        return atan2(self.real, self.im)
    
    def __str__(self):
        return f"{self.real} + {self.im}i"

if __name__ == "__main__":
    a = Komplex(2, 3)
    b = Komplex(4, 5)

    print("a =", a, "; b =", b)

    print("a + b =", a + b)
    print("a - b =", a - b)
    print("-a = ", -a)
    print("a * b = ", a * b)
    print("a / b = ", a / b)
    print("abs(a) = ", abs(a))
    print("a.arg() = ", a.arg())