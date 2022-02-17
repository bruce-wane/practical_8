class Data:
    @classmethod
    def data(cls, data):
        a = data.split('.')
        day = int(a[0])
        month = int(a[1])
        year = int(a[2])
        return day, month, year

    @staticmethod
    def validity(data):
        if data[0] < 1 or data[0] > 31:
            print('Wrong day')
        elif data[1] < 1 or data[1] > 12:
            print('Wrong month')
        elif data[2] < 2022:
            print('Wrong year')
        else:
            print('Correct date')

data = Data.data('23.12.2022')
Data.validity(data)

