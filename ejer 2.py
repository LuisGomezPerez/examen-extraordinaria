import random
class armaduras:
    def __init__(self, nombre,rango):
        self.nombre = nombre
        self.rango = rango
        print("Armadura creado")
    def __str__(self):
        return self.nombre + " " + self.rango
    
class calificacion(armaduras):
    def __init__(self, nombre,rango):
        super().__init__(nombre,rango)
    def __str__(self):
        return "Codigo_Legion: "+ self.nombre + " Identificacion de Cohorete: "  + self.rango[0] + " Identificador de siglo: " + self.rango[1]+ " identificador de escuadra: " + self.rango[2]+" Numero de trooper: "+self.rango[3]

a=armaduras("MK","8888")
b=armaduras("TP","8785")
lista=[a,b]
a=calificacion("TK","8654")
b=calificacion("FN","8654")
lista=[a,b]
for i in lista:
    print(i)