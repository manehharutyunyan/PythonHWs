class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def addition(self):
        print(self.x + self.y)
    
    def subtraction(self):
        print(self.x - self.y)
    
class  MyCalculation(Calculation):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def multiplication(self):
        print(self.x * self.y)
    
    def division(self):
        print(self.x / self.y)
        
c1 = Calculation(3, 5)
c1.subtraction()
c1.addition()
c2 = MyCalculation(3, 5)
c2.multiplication()
c2.division()
c2.subtraction()
c2.addition()