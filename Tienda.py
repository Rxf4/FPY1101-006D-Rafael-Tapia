'''----------AQUI VENDEMOS----------
'''

import os


print (50*'*')
print('Administracion de Stock'.center(50,'*'))
print(50*'*')

#Colecciones
productos = ('Escoba', 'Huevos', 'Leche','Harina')
inicio = ['Ver stock de productos','Añadir nuevo producto','Ajustar stock','Eliminar producto','Salir']


#Menú
while True:
    for ind in enumerate(inicio):

        print(f'{ind+1}.{inicio[ind]}')

    ans = input('¿Que quieres hacer?\n')

    if ans == '1':
        os.system('cls')
        for a,b in productos.items():
             print(f'{a}.{b}')
             print()
       
    elif ans == '2':
        os.system('cls')


    elif ans == '3':
        pass

    elif ans == '4':
        pass



    
    



    

    



   
