import math

class DualNumber:
    def __init__(self, value, dvalue):
        self.value = value
        self.dvalue = dvalue

    def __add__(self, other):
        z = DualNumber(self.value + other.value, 
            self.dvalue + other.dvalue)
        return z

    def __mul__(self, other):
        z = DualNumber(self.value * other.value,
            self.dvalue * other.value + other.dvalue * self.value)
        return z

    def __str__(self):
        return str(self.value) + " + " + str(self.dvalue) + "ε"

def sin(x):
    z = DualNumber(math.sin(x.value), math.cos(x.value)*x.dvalue)
    return z

x = DualNumber(0.5, 1)
y = DualNumber(4.2, 0)
z = x * y + sin(x)

print(z)

assert abs(z.value - 2.579425538604203) <= 1e-15
assert abs(z.dvalue - (y.value + math.cos(x.value))) <= 1e-15

x = DualNumber(0.5, 0)
y = DualNumber(4.2, 1)
z = x * y + sin(x)
assert abs(z.dvalue - x.value) <= 1e-15