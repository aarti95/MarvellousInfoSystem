class Demo:
    value = 10      ##class variable
    def __init__(self,no1,no2):
        print("Inside init method")
        self.i = no1
        self.j = no2
    def fun(self):   ##method
        print("Inside fun")
        print(self.i,self.j)
    def gun(self):
        print("Inside gun")
        print(self.i, self.j)

# Create object of Demo class

obj1 = Demo(11,21)
obj2 = Demo(51,101)

# Call the method fun
obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()

