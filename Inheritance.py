from OOPS import Calculator


class Inherit(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getcompletedata(self):
        return self.num2 + self.num + self.Summation()


obj = Inherit()
print(obj.getcompletedata())
