class Calculator:
    num = 100

    def getdata(self):
        print("I am now executing as method in class")

obj= Calculator()
obj.getdata()
print(obj.num)

#with constructor

class Calculator:
    num = 100
    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("Iam called automatically when object is created")

    def getdata(self):
        print("im now executing as method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber + self.num


obj= Calculator(2, 3)
obj.getdata()
print(obj.Summation())

obj1= Calculator(4, 5)
obj1.getdata()
print(obj1.Summation())