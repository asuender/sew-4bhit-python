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
        return f"{self.real} + {self.im}i"
    
    def __str__(self):
        return f"{self.real} + {self.im}i"

if __name__ == "__main__":
    a = Komplex(1, 2)
    b = Komplex(3, 4)

    print(a + b)
    print(a - b)
    print(-a)
    print(a * b)
    print(a / b)
    print(abs(a))
    print(a.arg())