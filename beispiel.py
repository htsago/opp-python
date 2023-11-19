class Basiklasse:

    def __init__(self, name):
        self.name = name

    def sagHallo(self):
        return f"Name: {self.name}"
    
    def addMe (self, arg1 ,arg2):
        arg3 = arg1 +arg2
        return arg3

class Erweiterklasse(Basiklasse):

    def zeigMich(self):
        return "Das bin ich"
    





    
obj = Erweiterklasse("Herman")
print(obj.sagHallo())
print(obj.zeigMich())
print(obj.addMe(2,5))


