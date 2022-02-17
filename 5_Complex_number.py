class complexNumber:
    def __init__(self, real, imgag):
        self.real = real
        self.imag = imgag

    def __add__(self, other):
        return complexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return complexNumber(self.real * other.real, self.imag * other.imag)

    def __str__(self):
        return f"Resualt: {self.real} + {self.imag}i"

com_num_a = input('Enter complex number a: ')
com_num_b = input('Enter complex number b: ')
try:
    a = complexNumber(int(com_num_a[0]), int(com_num_a[2]))
    b = complexNumber(int(com_num_b[0]), int(com_num_b[2]))
    print(a + b)
    print(a * b)
except ValueError:
    print('Enter a complex number of format a+bi')