from Electrodomestico import Electrodomestico

class Microondas(Electrodomestico):
    def __init__(self, codigo, precio, marca, color,control):
        super().__init__(codigo, precio, marca, color)
        self.control=control
        self.tipo='Microondas'


    


    def mostrar(self):
        print(f'\n----{self.tipo}----')
        print('     codigo producto:',self.codigo_producto)
        print('     precio: $',self.precio)
        print('     marca:',self.marca)
        print('     color:',self.color)
        print('     control digital:',self.control)