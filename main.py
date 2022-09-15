import random
import time
import sys

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[38m'

puntaje = random.randint(50,
                         101)  #Aqui guardaremos el puntaje del participante

iniciar_trivia = True
intentos = 0
bien = 0
mal = 0

while iniciar_trivia == True:

    def mecanografiar(texto):

        lista = texto.split()

        for palabra in lista:
            sys.stdout.write(palabra + " ")
            sys.stdout.flush()
            time.sleep(0.5)

    print("\n")
    mecanografiar(GREEN + "ESTAS POR EMPEZAR UN TEST DE MAGIA!" + WHITE)
    print("\n")
    intentos += 1
    puntaje = random.randint(50, 101)

    time.sleep(2)
    print("\nBienvenido a mi primera trivia sobre Harry Potter")
    print('Pondremos a prueba tus conocimientos de magia')

    time.sleep(1)

    print('\nEste es tu intento número: ', intentos)

    input(RED + '\nPRESIONA ENTER PARA PROBAR TU SUERTE: ')

    print(
        BLUE +
        '\nDe acuerdo a la suerte de la magia inicias con un puntaje de',
        puntaje, 'puntos' + WHITE)

    time.sleep(1)

    nombre = str(input('\nIngrese su nombre: '))

    print(
        '\nHola' + RED, nombre, WHITE +
        'responde las siguientes preguntas escribiendo la letra de la alternativa y presiona "enter" para enviar tu respuesta.\n'
    )

    time.sleep(4)

    print(
        GREEN +
        '\nSU PRUEBA DE CONOCIMIENTOS COMENZARÁ EN 5 SEGUNDOS... ESTÁS LISTO?\n'
        + WHITE)

    for numero_carga in range(5, 0, -1):
        print(numero_carga)
        time.sleep(1)

    #Pregunta 1
    print(RED + '\nPregunta 1. A qué casa se va Harry Potter?\n' + WHITE)
    a = 'a. Slytherin'
    b = 'b. Revencalw'
    c = 'c. Gryffyndor'
    d = 'd. Hufflepuff'

    time.sleep(2)

    print(a)
    print(b)
    print(c)
    print(d)

    respuesta1 = input('\nTu respuesta: ').lower()

    while respuesta1 not in ('a', 'b', 'c', 'd'):
        respuesta1 = input(
            'Debes responder a, b,c o d. Ingresa nuevamente tu respuesta: ')

    if respuesta1 == 'c':
        puntaje += random.randint(10, 20)
        print(GREEN + '\nMuy bien pequeño mago', nombre, '!')
        print('Alcanzaste', puntaje, 'puntos' + WHITE)
    else:
        puntaje -= random.randint(5, 10)
        print(RED + '\nIncorrecto!,', nombre, '!' + WHITE)
        print('Alcanzaste', puntaje, 'puntos')

    #PREGUNTA 2

    time.sleep(1)

    print(RED +
          '\nPregunta 2. Selecciona cual no es una Maldicion imperdonable\n' +
          WHITE)

    a = 'a. Imperio'
    b = 'b. cruciatus'
    c = 'c. bombardo'
    d = 'd. Avada Kedavra'

    time.sleep(2)

    print(a)
    print(b)
    print(c)
    print(d)

    respuesta2 = input('\nTu respuesta: ').lower()

    while respuesta2 not in ('a', 'b', 'c', 'd', 'x'):
        respuesta2 = input(
            'Debes responder a, b,c o d. Ingresa nuevamente tu respuesta: ')

    if respuesta2 == 'x':
        puntaje += 50
        print('Este es un mensaje secreto')
        print('Alcanzaste', puntaje, 'puntos')

    if respuesta2 == 'a':
        puntaje -= 10
        print(
            RED + '\nIncorrecto!'+
            WHITE, nombre,
            'Imperio si es una maldición inperdonable, sucio mouggle')
        print('Alcanzaste', puntaje, 'puntos')
    elif respuesta2 == 'b':
        puntaje -= 10
        print(RED + '\nIncorrecto!'+
            WHITE, nombre,
              'Cruciatus si es una maldición inperdonable, sucio muggle')
        print('Alcanzaste', puntaje, 'puntos')
    elif respuesta2 == 'd':
        puntaje -= 10
        print(
            RED + '\nIncorrecto!'+
            WHITE, nombre,
            'Avada kedavra si es una maldición inperdonable, sucio muggle' )
        print('Alcanzaste', puntaje, 'puntos')
    else:
        puntaje += 10
        print(GREEN + '\nMuy bien pequeño mago,', nombre, '!')
        print('Alcanzaste', puntaje, 'puntos' + WHITE)

    # PREGUNTA 3

    time.sleep(1)
    print(RED +
          '\nPregunta 3. ¿Las lágrimas de qué animal son el único antídoto conocido contra el veneno de basilisco?\n' +
          WHITE)

    a = 'a. billywig'
    b = 'b. Fénix'
    c = 'c. Hipogrifo'
    d = 'd. Boggart'

    time.sleep(2)

    print(a)
    print(b)
    print(c)
    print(d)

    respuesta2 = input('\nTu respuesta: ').lower()

    while respuesta2 not in ('a', 'b', 'c', 'd', 'x'):
        respuesta2 = input(
            'Debes responder a, b,c o d. Ingresa nuevamente tu respuesta: ')

    if respuesta2 == 'x':
        puntaje += 50
        print('Este es un mensaje secreto')
        print('Alcanzaste', puntaje, 'puntos')

    if respuesta2 == 'a':
        puntaje -= 10
        print(
            RED + '\nIncorrecto!'+
            WHITE, nombre,
            'sucio mouggle')
        print('Alcanzaste', puntaje, 'puntos')
    elif respuesta2 == 'c':
        puntaje -= 10
        print(RED + '\nIncorrecto!'+
            WHITE, nombre,
              'sucio muggle')
        print('Alcanzaste', puntaje, 'puntos')
    elif respuesta2 == 'd':
        puntaje -= 10
        print(
            RED + '\nIncorrecto!'+
            WHITE, nombre,
            'sucio muggle' )
        print('Alcanzaste', puntaje, 'puntos')
    else:
        puntaje += 10
        print(GREEN + '\nMuy bien pequeño mago,', nombre, '!')
        print('Alcanzaste', puntaje, 'puntos' + WHITE)
    time.sleep(2)
    print("\n")
    mecanografiar(MAGENTA + 'ESO ESTUVO INCREIBLE PEQUEÑO MAGO\n')
    print(MAGENTA + 'Gracias', nombre, 'por jugar mi trivia, alcanzaste',
          puntaje, 'puntos' + WHITE) 

    print("\n¿Deseas intentar la trivia nuevamente?")
    time.sleep(2)
    repetir_trivia = input(
        "\nIngresa 'si' para repetir, o cualquier tecla para finalizar: "
    ).lower()  #El "loxer" convierte a todo lo que ingresas en minusculas

    if repetir_trivia != "si":  # != significa "distinto"
        print(MAGENTA + '\nEspero, ', nombre,
              'que lo hayas pasado bien, hasta pronto!\n' + WHITE)
        iniciar_trivia = False
