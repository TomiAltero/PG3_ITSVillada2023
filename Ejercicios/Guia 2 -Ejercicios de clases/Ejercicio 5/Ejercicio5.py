class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cargar(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def pagar_impuestos(self):
        return self.sueldo > 3000
    
    def cargar(self):
        super().cargar()
        self.sueldo = float(input("Ingrese el sueldo: "))
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo:", self.sueldo)


persona1 = Persona("Juan", 30)
persona1.imprimir()

empleado1 = Empleado("Pedro", 25, 4000)
empleado1.imprimir()
print("Debe pagar impuestos:", empleado1.pagar_impuestos())

empleado2 = Empleado("", 0, 0)
empleado2.cargar()
empleado2.imprimir()
print("Debe pagar impuestos:", empleado2.pagar_impuestos())
