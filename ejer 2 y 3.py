import string, random

class Nombre:
    def _init_(self, nombre):
        self.nombre = nombre


class Rango:
    def _init_(self, rango):
        self.rango = rango

class Armadura(Nombre, Rango):
    def _init_(self,nombre,rango):
        self.nombre=nombre;
        self.rango=rango;
        print(f'La armadura {self.rango} se ha creado con éxito')
        self.calificacion()

    def _str_(self):
        return '\nNombre: ' + self.nombre + '\nRango: ' + self.rango + '\nCodigo de legión: ' + self.codigo + '\nCiherente: ' + self.cihirente + '\nSiglo: ' + self.siglo + '\nArmadura: ' + self.armadura + '\nEscuadra: ' + self.escuadra

    def calificacion(self):
        temp = self.nombre.split('-')
        print("temp: "+ str(temp))
        self.codigo = temp[0]
        temp = temp[1]
        self.cihirente = temp[0]
        self.siglo = temp[1]
        self.armadura = temp[2]
        self.escuadra = temp[3]
       

def experimentacion(n):
        lista_arm = []
        for _ in range(n):
            nombre = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + '-'
            for _ in range(4):
                nombre += str(random.randint(0, 9))

            armadura = Armadura(nombre,'Soldier')
            lista_arm.append(armadura)

        for i in lista_arm:
            print(i)

        return lista_arm

experimentacion(10)