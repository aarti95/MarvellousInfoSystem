class Circle():
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

# Accept method will accept value of Radius from user.

    def Accept(self):
        self.Radius = int(input("Enter the radius of the circle"))
        return self.Radius

# CalculateArea() method will calculate area of circle and store it into instance variable Area.
    def CalculateArea(self):
        self.Area = self.PI * self.Radius **2
        return self.Area

# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
    def CalculateCircumference(self):
        self.Circumference= 2 * self.PI * self.Radius
        return self.Circumference

# And Display() method will display value of all the instance variables as Radius , Area, Circumference
    def Display(self):
        print("Radius is",self.Radius )
        print("Area is ",self.Area )
        print("Circumference is",self.Circumference)

nu = Circle()
nu.Accept()
k = nu.CalculateArea()
n = nu.CalculateCircumference()
nu.Display()