class officeEquipment:
    storage = {}
    def __init__(self, model, color, paperSize, weight, number):
        self.model = model
        self.color = color
        self.paperSize = paperSize
        self.weight = weight
        self.number = number

class Printer(officeEquipment):
    def __init__(self, model, color, paperSize, weight, number, colorPrint, techPrint):
        super().__init__(model, color, paperSize, weight, number)
        self.colorPrint = colorPrint
        self.techPrint = techPrint

    def Dirprinter(self):
        officeEquipment.storage['Office equipment'] = 'Printer'
        officeEquipment.storage['Model'] = self.model
        officeEquipment.storage['Color'] = self.color
        officeEquipment.storage['Paper size'] = self.paperSize
        officeEquipment.storage['Weight'] = self.weight
        officeEquipment.storage['Color print'] = self.colorPrint
        officeEquipment.storage['Tech print'] = self.techPrint
        officeEquipment.storage['Number'] = int(self.number)
        print(officeEquipment.storage)


class Scanner(officeEquipment):
    def __init__(self, model, color, paperSize, weight, number, scanSpeed):
        super().__init__(model, color, paperSize, weight, number)
        self.scanSpeed = scanSpeed

    def Dirscaner(self):
        officeEquipment.storage['Office equipment'] = 'Scaner'
        officeEquipment.storage['Model'] = self.model
        officeEquipment.storage['Color'] = self.color
        officeEquipment.storage['Paper size'] = self.paperSize
        officeEquipment.storage['Weight'] = self.weight
        officeEquipment.storage['Scan speed'] = self.scanSpeed
        officeEquipment.storage['Number'] = self.number
        print(officeEquipment.storage)

offEqu = input('Enter office equipment: ')
if offEqu == 'Printer':
    try:
        printer = Printer(input('Enter model: '), input('Enter color: '), input('Enter paper size: '), input('Enter weight: '),
                    int(input('Enter number: ')), input('Enter color print: '),input('Enter tech print: '))
    except ValueError:
        print('Wrong number')
        printer = Printer(input('Enter model: '), input('Enter color: '), input('Enter paper size: '), input('Enter weight: '),
                    int(input('Enter number: ')), input('Enter color print: '), input('Enter tech print: '))
    printer.Dirprinter()
elif offEqu == 'Scaner':
    try:
        scaner = Scanner(input('Enter model: '), input('Enter color: '), input('Enter paper size: '), input('Enter weight: '),
                    int(input('Enter number: ')), input('Enter scan speed: '))
    except ValueError:
        print('false')
        scaner = Scanner(input('Enter model: '), input('Enter color: '), input('Enter paper size: '), input('Enter weight: '),
                    int(input('Enter number: ')), input('Enter scan speed: '))
    scaner.Dirscaner()



