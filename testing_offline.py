from hero import Hero
import os
from time import sleep
castillos = ['Fermat', 'Lagrange', 'Newton', 'Gauss', 'Neumann']

# print('Bienvenido a este raro juego')
# nombre = input('Introduzca su nombre: ')

# print('Seleccione un castillo')
# print('0 - ', castillos[0], '\n1 - ', castillos[1], '\n2 - ', castillos[2], '\n3 - ', castillos[3], '\n4 - ', castillos[4])

# castillo = castillos[int(input())]

# _hero = Hero(castillo, nombre)
# _hero = Hero(castillos[4], 'Lemas')

# print(_hero)

# while(1):
#     print('Que desea hacer?')
#     print('0 - Me\n1 - Forest\n2 - Quit')

#     response = int(input())

#     if response == 2:
#         break
#     elif response == 1:
#         _hero.Forest()
#     elif response == 0:
#         print(_hero)



file = os.open('testt',os.O_RDWR + os.O_CREAT)
ff = bytearray
while(True):
    piece = os.read(file,4096)
    if(piece == b''):
        break
    sleep(1)
    print(piece)