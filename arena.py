from threading import Timer

# Cuando un heroe esta buscando batallas en la arena
# entra en este diccionario y ve si hay alguien de su
# mismo nivel, si hay alguien los empareja para que
# luchen, de lo contrario se agrega este heroe en la
# espera de otro de su mismo nivel
# Dictionary<int(level), Hero>
heroes = {}