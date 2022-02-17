class Div:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def division(self):
        try:
            resualt = self.num_1 / self.num_2
        except ZeroDivisionError:
            return 'Zero division error'
        return resualt

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

class_del = Div(num_1, num_2)
resualt = Div.division(class_del)
print(resualt)
