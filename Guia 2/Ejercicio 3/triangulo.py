class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.lados = [lado_a, lado_b, lado_c]
        
    def lado_mayor(self):
        print(max(self.lados))

triangulo1 = Triangulo(2 , 5 , 9)
triangulo1.lado_mayor()