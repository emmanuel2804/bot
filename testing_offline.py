from hero import Hero

castillos = ['Fermat', 'Lagrange', 'Newton', 'Gauss', 'Neumann']

print('Bienvenido a este raro juego')
nombre = input('Introduzca su nombre: ')

print('Seleccione un castillo')
print('0 - ', castillos[0], '\n1 - ', castillos[1], '\n2 - ', castillos[2], '\n3 - ', castillos[3], '\n4 - ', castillos[4])

castillo = castillos[int(input())]

_hero = Hero(castillo, nombre)

print(_hero)