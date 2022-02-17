class Checklist:
    array = []
    def __init__(self, usernum):
        self.usernum = usernum

    @classmethod
    def Array(cls, usernum):
        if usernum == 'stop':
            print(Checklist.array)
        else:
            try:
                int_num = int(usernum)
                Checklist.array.append(int_num)
                Checklist.Array(input('Enter number: '))
            except ValueError:
                print('false')
            else:
                Checklist.Array(input('Enter number: '))

Checklist.Array(input('Enter number: '))