class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def mostrar_atributos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
        
    def verif_aprobado(self):
        if self.nota >= 6:
            print("El alumno esta aprobado")
        else:
            print("El alumno esta desaprobado")

alumno1 = Alumno("Tomas Altero", 8)
alumno2 = Alumno("Alejo Vaquero", 2)

alumno1.mostrar_atributos()
alumno1.verif_aprobado()


alumno2.mostrar_atributos()
alumno2.verif_aprobado()

