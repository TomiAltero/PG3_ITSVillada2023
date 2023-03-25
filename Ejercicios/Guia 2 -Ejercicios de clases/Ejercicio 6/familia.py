class Familia:
    def __init__(self,padre, madre, hijos= []):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        
    def __str__(self):
        hijos_str = ""
        
        for i in self.hijos:
            hijos_str += i + ", "
        hijos_str = hijos_str.rstrip(", ")
        
        return f"Padre: {self.padre}, Madre: {self.madre}, Hijos: {hijos_str}"

familia1 = Familia("Juan", "Maria", ["Pedro", "Alejo", "Tomas"])

print(familia1)
