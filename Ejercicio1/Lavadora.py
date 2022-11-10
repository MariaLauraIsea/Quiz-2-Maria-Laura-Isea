from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, codigo, precio, marca, color,capacidad):
        super().__init__(codigo, precio, marca, color)
        self.capacidad=capacidad
        self.tipo='Lavadora'




    def mostrar(self):
        print(f'\n----{self.tipo}----')
        print('     codigo producto:',self.codigo_producto)
        print('     precio: $',self.precio)
        print('     marca:',self.marca)
        print('     color:',self.color)
        print('     capacidad:',self.capacidad)
        