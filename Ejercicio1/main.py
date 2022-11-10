#============================
#nombre: Maria Laura Isea
#carnet: 20221110255
#============================

from Lavadora import Lavadora
from Microondas import Microondas
from Nevera import Nevera
from Licuadora import Licuadora

def registrar(edd):
    electrodomesticos=[]
    for e,info in edd.items():
        if e=='washer':
            for l in info:
                electrodomestico=Lavadora(l['cod_p'],l['price'],l['brand'],l['color'],l['capacity'])
            
                electrodomesticos.append(electrodomestico)

        elif e=='microwave':
            for m in info:
                electrodomestico=Microondas(m['cod_p'],m['price'],m['brand'],m['color'],m['digital'])
                
                electrodomesticos.append(electrodomestico)

        elif e=='fridge':
            for f in info:
                electrodomestico=Nevera(f['cod_p'],f['price'],f['brand'],f['color'],f['cooler'],f['comp'])
                
                electrodomesticos.append(electrodomestico)
        
        else:
            for b in info:
                electrodomestico=Licuadora(b['cod_p'],b['price'],b['brand'],b['color'],b['cup'],b['speeds'])
                
                electrodomesticos.append(electrodomestico)


    return electrodomesticos
        
        
        
def get_opcion():
    while True:
        try:
            opcion=int(input('Seleccione la accion que desee realizar:\n1-Leer Inventario\n2-Borrar producto defectuoso\n3-Mostrar datos extra\n4-Salir\n=> '))
            if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4:
                raise Exception

        except:
            print('\ningreso invalido!\n')

        return opcion


def get_eliminar(electrodomesticos):
    
    try:
        eliminar=input('\ningrese el codigo del producto defectuoso a eliminar: ').upper()
        
    
        for e in electrodomesticos:
            if eliminar!=e.codigo:
                raise Exception
                    

    except:
        print('\nERROR no se ha encontrado un producto con ese codigo, intente de nuevo\n')

    return eliminar


def producto_costoso(electrodomesticos):
    mas_costoso=0
    producto_costoso=None
    for e in electrodomesticos:
        if e.precio>=mas_costoso:
            producto_costoso=e

    return producto_costoso



def main():
    edd = {
    "washer":
    [
        {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
        {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
    ],
    "microwave":
    [
        {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
        {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
    ],
    "fridge":
    [
        {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
        {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
    ],
    "blender":
    [
        {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
        {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
    ]
}
    electrodomesticos=registrar(edd)
    productos_borrados=[]
    
    print('---BIENVENIDO A VENTAS NARANJA---')
    while True:
        opcion=get_opcion()

        if opcion==1:
            print('---INVENTARIO DE VENTAS NARANJA---')
            for e in electrodomesticos:
                #tipo=e.tipo
                e.mostrar()

        elif opcion==2:
            for e in electrodomesticos:
                e.mostrar()

            eliminar=get_eliminar(electrodomesticos)

            for e in electrodomesticos:
                if eliminar==e.codigo_producto:
                    productos_borrados.append(e)
                    electrodomesticos.remove(e)
                    print('\nse ha eliminado el producto de la base de datos!\n')

        elif opcion==3:
            print('\n---EQUIPOS ELIMINADOS POR DEFECTOS---')
            if len(productos_borrados)==0:
                print('\nno se han eliminado productos de la base de datos!\n')
            else:
                for p in productos_borrados:
                    p.mostrar()


            print('\n---NEVERAS DISPONIBLES---')
            for e in electrodomesticos:
                if e.tipo=='Nevera':
                    print(f'\n----{e.tipo}----')
                    print('     codigo producto:',e.codigo_producto)
                    print('     incluye congelador:',e.inc_congelador)
            
            
            
            #prod_mas_costoso=producto_costoso(electrodomesticos)
            #print('\n----EQUIPO MAS COSTOSO----')
            #prod_mas_costoso.mostrar()

            pass
            

        else:
            break

    



main()