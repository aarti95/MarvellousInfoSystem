class Arithematic():
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first number"))
        self.value2 = int(input("Enter second number"))

    def Addition(self):
        self.Addition = self.value1+self.value2
        return self.Addition

    def Substraction(self):
        self.Substraction = self.value1-self.value2
        return self.Substraction

    def Mutliply(self):
        self.Mutliply = self.value1 * self.value2
        return self.Mutliply

    def Division(self):
        self.Division = self.value1 // self.value2
        return self.Division

    def Display(self):
        print("Addition is ", self.Addition)
        print("Subtraction is ", self.Substraction)
        print("Mulitplication is", self.Mutliply)
        print("Division is ",self.Division)


obj1 = Arithematic()
obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Mutliply()
obj1.Division()
obj1.Display()

obj2 = Arithematic()
obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Mutliply()
obj2.Division()
obj2.Display()





