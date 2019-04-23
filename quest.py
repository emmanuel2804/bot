from random import Random

# este diccionario va a contener las preguntas que te pueden salir
# haciendo un quest, la llave del diccionario es el lvl del jugador
# y el valor es una lista que contiene tuplas donde se almacena
# en la primera posicion la pregunta y en la segunga la respuesta
# Dictionary<int, List<Tuple<string, int, List<posibles respuestas>>>> questions
questions = {}

for i in range(1, 31):
    questions[i] = []

questions[1].append(('Cuanto es 2+2?', 4, (2, 1, 5, 4)))
questions[1].append(('La raiz cuadrada de 100 es ...', 10, (1, 10, 50, 25)))
questions[1].append(('12 * 12', 144, (121, 255, 128, 144)))
questions[1].append(('2 elevado a la 10', 1024, (1024, 400, 512, 4000)))
questions[1].append(('1 + 1 + 1 + 1 * 0 + 1', 1, (2, 4, 5, 1)))
questions[1].append((str(Random.random()) + ' elevado a la 0', 1, (Random.random(), 0.5, 1, 0)))

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