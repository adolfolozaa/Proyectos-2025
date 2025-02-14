
import pprint
import numpy as np

#Inicializado cada jugador
mat_A = np.zeros ((8,  8))
mat_B = np.zeros ((8,  8))

def ingreso(jugador):
    naves = [1, 1, 1, 2]
    #print(jugador)
    if jugador == 'A':
        matriz = mat_A
        ingreso_nave(jugador,matriz, naves)
    else:
        matriz = mat_B
        ingreso_nave(jugador, matriz, naves)
          
jugador_1= None
jugador_2 = None
def inicio():
    
    jugador = input('Ingrese el jugador (A o B):  ').upper()
    if jugador == 'A':
        print(f'Welcome  Player {jugador}')
        ingreso(jugador)
        print('Ingrese Player B')
        inicio()

    elif jugador == 'B':
        print(f'Welcome  Player {jugador}')
        ingreso(jugador)
      
    else:
        print('Ingreso no valido')
        inicio()

def jugar():
    turno = 0
    if turno == 0:
        print("Es el turno del jugador 'A'")
        print(mat_A)
        tiro = input('pon las coordenadas donde quieres disparar (ejemplo: A1):')
        tiro_H = tiro[0].upper()
        tiro_V = tiro[1]
        print(tiro_H + '  ' + tiro_V)
    elif turno == 1:
        print("Es el turno del jugador 'B'")
        print(mat_B)
        tiro = input('pon las coordenadas donde quieres disparar (ejemplo: A1):')
        tiro_H = tiro[0].upper()
        tiro_V = tiro[1]
        print(tiro_H + '  ' + tiro_V)


def ingreso_nave(jugador, mat, naves):
    print(f'por favor coloque sus naves jugador {jugador}')
    equiv_fila = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

    for nave in naves:
        if nave == 1:
            x = input('elija la fila (A..H) casilla? ')
            x1 = equiv_fila.get(x.upper())-1
            y = int(input('elija la columna (1..8) casilla? ')) - 1
            print(f'Su nave ocupara la posicion: {x.upper()}{y+1}')
            mat[x1][y] = nave
        else:
            print('Elija dos filas o dos columnas contiguas')
            modo = input('Su nave va a estar de modo vertical u horizontal (H o V?  ').upper()
            if modo == 'H':
                print('MODO HORIZONTAL: elija 1 fila y 2 columnas')
                x = input('elija la fila (A..H) casilla? ')
                x1 = equiv_fila.get(x.upper())-1
                y_1 = int(input('elija la columna (1..8) casilla? ')) - 1
                y_2 = int(input('elija la columna (1..8) casilla? ')) - 1
                print(f'Su nave ocupara las posiciones : {x.upper()}{y_1+1} y {x.upper()}{y_2+1}')
                mat[x1][y_1] = nave
                mat[x1][y_2] = nave
                
            else:
                print('MODO VERTICAL: elija 2 filas y 1 columna')
                x_1 = input('elija la fila (A..H) casilla? ')
                x1 = equiv_fila.get(x_1.upper())-1
                x_2 = input('elija la fila (A..H) casilla? ')
                x2 = equiv_fila.get(x_2.upper())-1
                y = int(input('elija la columna (1..8) casilla? ')) - 1
                print(f'Su nave ocupara las posiciones : {x_1.upper()}{y+1} y {x_2.upper()}{y+1}')
                mat[x1][y] = nave
                mat[x2][y] = nave
      
    pprint.pprint(mat)

  
inicio()
jugar()








'''player_A = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
            ]
#pprint.pprint(player_A)
for x in range(6):
    for y in range(6):
        player_A[x][y] = random.randint(0, 2)
pprint.pprint(player_A)
'''

