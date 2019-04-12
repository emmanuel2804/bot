from random import Random

# este diccionario va a contener las preguntas que te pueden salir
# haciendo un quest, la llave del diccionario es el lvl del jugador
# y el valor es una lista que contiene tuplas donde se almacena
# en la primera posicion la pregunta y en la segunga la respuesta
# Dictionary<int, List<Tuple<string, int>>> questions
questions = {}

def Forest(lvl):
    temp = Random()

    # las preguntas van a salir con una probabilidad de 0.3, en otro
    # caso solo vas al bosque y viras con cierto exp y gold
    if(temp.uniform(0, 1) >= 0.3):
        return None

    # me quedo con las posibles preguntas que le puedo hacer a este
    # jugador
    posible = questions[lvl]

    # retorno una tupla de (pregunta, respuesta) para que la clase
    # Hero la maneje, si la respuesta dada por el jugador es correcta
    # entonces almacena la pregunta para utilizarla despues en duelos
    return temp.choice(posible)