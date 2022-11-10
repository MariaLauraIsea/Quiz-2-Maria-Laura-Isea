from Electrodomestico import Electrodomestico

class Licuadora(Electrodomestico):
    def __init__(self, codigo, precio, marca, color,material,velocidades):
        super().__init__(codigo, precio, marca, color)
        self.material_vaso=material
        self.velocidades=velocidades
        self.tipo='Licuadora'

    


    def mostrar(self):
        print(f'\n----{self.tipo}----')
        print('     codigo producto:',self.codigo_producto)
        print('     precio: $',self.precio)
        print('     marca:',self.marca)
        print('     color:',self.color)
        print('     material vaso:',self.material_vaso)
        print('     veocidades:',self.velocidades)