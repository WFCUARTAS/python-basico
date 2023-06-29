import random
import time
from pynput import keyboard as kb
import  sys


#INICIALICAR LOS VALORES PARA PINTAR EN PANTALLA
tam_x = 100
tam_y=10
l_completa=    '*'
l_intermedias ='*'
for i in range(tam_x):
    l_completa    += '*'
    l_intermedias += ' '
l_completa    += '*'
l_intermedias += '*'

def print_line(text):
    t = tam_x - len(text)
    text_def = '*'

    for i in range(int(t / 2)):
        text_def += ' '
    text_def += text
    for i in range(int(t / 2)):
        text_def += ' '
    if int(t) % 2 == 0:
        text_def += '*'
    else:
        text_def += ' *'
    print(text_def)

def print_salto(n):
    for i in range(n):
        print(l_intermedias)

#FUNCION QUE INPRIME EN EL RECUADRO LO QUE SE LE EVNIA
def pantalla(text):
    print('\n\n\n\n\n\n\n\n\n\n\n\n'+l_completa)

    list_texto = text.split('\n')
    tam=int((tam_y-len(list_texto))/2)

    print_salto(tam)
    for t in list_texto:
        print_line(t)
    print_salto(tam)

    if len(list_texto)%2 != 0:
        print_salto(1)

    print(l_completa)

#VARIABLES GLOBALES
opciones=['piedra','papel','tijera']

reglas = {
    'piedra' : 'tijera',
    'papel'  :  'piedra',
    'tijera' : 'papel'
}

inicio = False
jugando= True
selecion=1

pantalla('Bienbenido al juego Piedra, Papel o Tijera\n\nPara una mejor experiencia ajusta el tamaño de la consola\nasegurate que puedes ver todo el marco de asteriscos\npreciona cualquier tecla para iniciar')

#LOGICA DEL JUEGO VALIDACION DEL GANADOR
def jugar():
    maquina = random.choice(opciones)
    jugador = opciones[int(selecion) - 1]

    win=f'Jugador: {jugador}\nMaquina: {maquina}\n\n'
    if reglas[maquina] == jugador:
       win +='** LA MAQUINA GANO **'
    elif maquina == jugador:
        win+='** EMPATE **'
    else:
        win+='** EL JUGADOR GANO **'

    pantalla(win)



def Menu_seleccion(tecla):
    global selecion, jugando
    reload=False

    if tecla == kb.KeyCode.from_char('a') and selecion>1:
        selecion -=1
        reload = True
    elif tecla == kb.KeyCode.from_char('d') and selecion<3:
        selecion += 1
        reload = True
    elif tecla == kb.KeyCode.from_char('x'):
        sys.exit()

    if tecla == kb.Key.space and not jugando:
        jugando = True
        jugar()

    elif reload or jugando:
        jugando = False
        tex='selecciona una opción (usa a - d)\n'
        if selecion==1:
            tex+='Piedra(*)  -  Papel( )  -  Tijera( )'
        elif selecion==2:
            tex += 'Piedra( )  -  Papel(*)  -  Tijera( )'
        else:
            tex += 'Piedra( )  -  Papel( )  -  Tijera(*)'

        tex+='\n\n ¡Preciona spacio para jugar!'

        pantalla(tex)

def pulsa(tecla):
    global inicio
    if not inicio:
        pantalla('Usa el teclado para navegar en el juego (A,D)\n ⬅ A     D ➡\n Spacio para Seleccionar\n\n¡Preciona cualquier tecla para iniciar! \n\n uaa X para salir en cualquier momento deal juego')
        inicio=True
    else:
        Menu_seleccion(tecla)

with kb.Listener(pulsa) as escuchador:
	escuchador.join()

