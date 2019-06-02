from random import Random

# este diccionario va a contener las preguntas que te pueden salir
# haciendo un quest, la llave del diccionario es el lvl del jugador
# y el valor es una lista que contiene tuplas donde se almacena
# en la primera posicion la pregunta y en la segunga la respuesta
# Dictionary<int, List<Tuple<string, int, List<posibles respuestas>>>> questions
questions = {}

for i in range(1, 31):
    questions[i] = []

questions[1].append(('esta pregunta es verdadera', 'verdadero', ('verdadero', 'falso')))
questions[1].append(('Si (0, 2, 5) y (1, 1, 1) son soluciones optimas de un problema de PL entonces (0, 1, 5) tambien lo es', 'falso', ('verdadero', 'falso')))
questions[1].append(('El numero maximo de variables diferentes de cero en una solucion factible basica de un sistema de ecuaciones lineales es igual al numero de restricciones', 'verdadero', ('verdadero', 'falso')))
questions[1].append(('Una condicion suficiente para que existan optimos multiples en un problema de PL es que exista algun indice j secundario con rj = 0', 'falso', ('verdadero', 'falso')))
questions[1].append(('Todas las operaciones que se realizan en una iteracion del Simplex equivalen a la solucion de 3 sistemas de ecuaciones lineales con la misma matriz del sistema de restricciones', 'verdadero', ('verdadero', 'falso')))
questions[1].append(('El simplex revisado consiste en añadir al metodo Simplex las reglas que permiten evitar el ciclo cuando hay degeneracion', 'falso', ('verdadero', 'falso')))
questions[1].append(('El criterio de entrada a la base garantiza la factibilidad de la nueva solucion basica', 'falso', ('verdadero', 'falso')))
questions[1].append(('Bajo hipotesis de no degeneracion el metodo Simplex realiza entre m y 3m/2 iteraciones y converge polinomialmente', 'falso', ('verdadero', 'falso')))

def Forest(lvl):
    temp = Random()

    # las preguntas van a salir con una probabilidad de 0.3, en otro
    # caso solo vas al bosque y viras con cierto exp y gold
    # if(temp.uniform(0, 1) >= 0.3):
    #     return None

    # me quedo con las posibles preguntas que le puedo hacer a este
    # jugador
    posible = questions[lvl]

    # retorno una tupla de (pregunta, respuesta) para que la clase
    # Hero la maneje, si la respuesta dada por el jugador es correcta
    # entonces almacena la pregunta para utilizarla despues en duelos
    return temp.choice(posible)