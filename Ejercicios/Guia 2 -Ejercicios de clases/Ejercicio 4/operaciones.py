class Operaciones:
    def __init__(self, num1 , num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2    
    
    def resta(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2
    
operaciones1 = Operaciones(5 , 8)

print(operaciones1.suma())
print(operaciones1.resta())
print(operaciones1.mult())
print(operaciones1.div())
    