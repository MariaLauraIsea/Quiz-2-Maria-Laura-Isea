from Electrodomestico import Electrodomestico

class Nevera(Electrodomestico):
    def __init__(self, codigo, precio, marca, color,congelador,compartimientos):
        super().__init__(codigo, precio, marca, color)
        self.inc_congelador=congelador
        self.compartimientos=compartimientos
        self.tipo='Nevera'


   

    def mostrar(self):
        print(f'\n----{self.tipo}----')
        print('     codigo producto:',self.codigo_producto)
        print('     precio: $',self.precio)
        print('     marca:',self.marca)
        print('     color:',self.color)
        print('     incluye congelador:',self.inc_congelador)
        print('     compartimientos:',self.compartimientos)