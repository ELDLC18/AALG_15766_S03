import random

class Perro:
    def __init__(self, nombre = "", color = "", edad = 0):
        self._nombre = nombre
        self._color = color
        self._edad = edad
    
    def ladrar(self):
        print("Guau")
    
    def saludo(self):
        return "Pata" if random.randint(0,1) == 0 else "Cola"
    
    def __str__(self):
        return f"Perro: {self._nombre}, de color {self._color} y tiene {self._edad} años"


p = Perro("Fido", "Marron", 5)
p.ladrar()
print(f"Me saludó con la {p.saludo()}")
print(p)
print()

q = Perro()
q = Perro("Rambo", "negro", 5)
print(q._nombre)          