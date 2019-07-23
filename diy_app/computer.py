class Computer:
    def __init__(self, model, year, manufacturer, type):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.type = type
    
    def get_computer_info(self):
        print(f"{self.manufacturer} {self.model} {self.year} ({self.type})")

class ComputerType:
    def __init__(self, type='desktop'):
        self.type = type

    def computer_type(self):
        if self.type == 'laptop':
            type = 'laptop'
        else:
            type = 'desktop'

        return self.type

        # print(f"This machine is {type} type")

class Desktop(Computer):
    def __init__(self, model, year, manufacturer, type):
        super().__init__(model, year, manufacturer, type)
        self.type = ComputerType()

    def describe_computer(self):
        # print(self.type)
        if self.type == 'desktop':
            type = ComputerType()
            print(type.computer_type())
        #     # print(f"It is {self.type}")
        
        #     computer_information = f"This is {self.manufacturer} from {self.model}, {self.year}"
        #     return computer_information

class Laptop(Computer):
    def __init__(self, model, year, manufacturer, type):
        super().__init__(model, year, manufacturer, type)
        self.type = ComputerType()
        # self.type = type

    def describe_computer(self, type='laptop'):
        print(self.type)

        # if self.type == type:
        #     type = ComputerType()
        #     print(type.computer_type())

        #     # print(f"It is {self.type}")
        
        #     computer_information = f"This is {self.manufacturer} from {self.model}, {self.year}"
        #     return computer_information

my_computer = Computer('apple', '2012', 'macpro', 'desktop')
# # print(my_computer)
my_computer.get_computer_info()

my_desktop = Desktop('apple', '2012', 'MacPro', 'desktop')
print(my_desktop.describe_computer())
my_desktop.get_computer_info()
# my_desktop.type.computer_type()

my_laptop = Laptop('apple', '2012', 'macbook pro', 'laptop')
print(my_laptop.describe_computer())
my_laptop.get_computer_info()
# my_laptop.type.computer_type()

