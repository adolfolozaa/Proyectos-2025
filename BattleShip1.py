
import pprint
import os
import numpy as np

#Inicializado cada jugador
mat_A = []
for y in range(5):
    # Agregamos un arreglo a la matriz, que sería una fila básicamente
    mat_A.append([])
    for x in range(5):
        # Y luego agregamos una celda a esa fila. Por defecto lleva "Mar"
        mat_A[y].append(' ')

mat_B= []
for y in range(5):
    # Agregamos un arreglo a la matriz, que sería una fila básicamente
    mat_B.append([])
    for x in range(5):
        # Y luego agregamos una celda a esa fila. Por defecto lleva "Mar"
        mat_B[y].append(' ')

print('Matriz del Jugador A')
pprint.pprint(mat_A)
print('----------------')
print('Matriz del Jugador B')
pprint.pprint(mat_B)
print('----------------\n')


def ingreso(jugador):
    naves = [1, 1, 1, 2]
    #print(jugador)
    if jugador == 'A':
        matriz = mat_A
        ingreso_nave(jugador, matriz, naves)
    else:
        matriz = mat_B
        ingreso_nave(jugador, matriz, naves)
          
jugador_1= None
jugador_2 = None
def inicio():
    
    jugador = "A" 
    print(f'Bienvenido  JUGADOR   {jugador}')

    ingreso(jugador)

    jugador = "B" 
    print('--------------------------------------------')

    print(f'Bienvenido  JUGADOR   {jugador}')
    ingreso(jugador)

def jugar():
    disparos = 0
    turno = 0
    while disparos < 16:
        if turno == 0:
            print("Es el turno del jugador 'A'")
            pprint.pprint(mat_A)
            tiro = input('pon las coordenadas donde quieres disparar (ejemplo: A1):')
            tiro_H = tiro[0].upper()
            tiro_H = equiv_fila.get(tiro[0].upper())-1
            tiro_V = int(tiro[1])-1
            if mat_B[tiro_H][tiro_V] == 1 or  mat_B[tiro_H][tiro_V] == 2:
                print('Disparo Acertado')
                mat_B[tiro_H][tiro_V] = '*'
            else: 
                print('Disparo fallido')
                mat_B[tiro_H][tiro_V] = '-'

            disparos += 1
            naves = cuenta_naves(mat_B)
            print(f'Naves disponibles Jugador B: {naves}')
            if naves == 0:
                print(' FIN DEL JUEGO, GANA JUGADOR A')
                break
            print(disparos//2)
            print(f'Naves disponibles Jugador A: {cuenta_naves(mat_A)}')

            turno = 1

        elif turno == 1:
            print("Es el turno del jugador 'B'")
            pprint.pprint(mat_B)
            tiro = input('pon las coordenadas donde quieres disparar (ejemplo: A1):')
            tiro_H = tiro[0].upper()
            tiro_H = equiv_fila.get(tiro[0].upper())-1
            tiro_V = int(tiro[1])-1
            if mat_A[tiro_H][tiro_V] == 1 or mat_A[tiro_H][tiro_V] == 2:
                print('Disparo Acertado')
                mat_A[tiro_H][tiro_V] = '*'
            else: 
                print('Disparo fallido')
                mat_A[tiro_H][tiro_V] = '-'

            disparos += 1
            naves = cuenta_naves(mat_A)
            print(f'Naves disponibles Jugador A: {naves}')
            if naves == 0:
                print(' FIN DEL JUEGO, GANA JUGADOR B')
                break
            print(disparos//2)
            turno = 0


def validar_fila(ubicacion):
        if (ubicacion[0].upper() in ['A', "B", 'C', 'D', 'E']) and (ubicacion[1] in ['1', '2', '3', '4', '5']):
                print(f'Ubicacion correcta {ubicacion}')
                return ubicacion
        else:
            ubicacion = input('elija una ubicacion valida (A..E) y (1..5) ? ') 
            return validar_fila(ubicacion)

equiv_fila = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

def ingreso_nave(jugador, mat, naves):
    print('--------------------------------------------\n\n')

    print(f'por favor coloque sus naves JUGADOR {jugador}')

    for nave in naves:
        if nave == 1:
            ubicacion = input('elija la fila (A..H) seguido de un numero (1..8? ')
            ubicacion = validar_fila(ubicacion)
            print(ubicacion)

            x = ubicacion[0]
            y = int(ubicacion[1])-1
            x1 = equiv_fila.get(x.upper())-1
            print(f'Su nave ocupara la posicion: {x.upper()}{y+1}')
            mat[x1][y] = nave
 
        else:
            print('Elija dos filas o dos columnas contiguas')
            modo = input('Su nave va a estar de modo vertical u horizontal (H o V?  ').upper()
            if modo == 'H':
                print('MODO HORIZONTAL: elija 1 fila y 2 columnas')
                ubicacion_1 = input('Ubicacion 1: elija la fila (A..E) seguido de un numero (1..5? ? ')
                ubicacion_2 = input('Ubicacion 2: elija la fila (A..E) seguido de un numero (1..5? ? ')
                x1 = equiv_fila.get(ubicacion_1[0].upper())-1
                y_1 = int(ubicacion_1[1]) - 1
                y_2 = int(ubicacion_2[1]) - 1
                print(f'Su nave ocupara las posiciones : {ubicacion_1[0].upper()}{y_1+1} y {ubicacion_1[0].upper()}{y_2+1}')
                mat[x1][y_1] = nave
                mat[x1][y_2] = nave

                
            else:
                print('MODO VERTICAL: elija 2 filas y 1 columna')
                ubicacion_1 = input('Ubicacion 1: elija la fila (A..E) seguido de un numero (1..5? ? ')
                x1 = equiv_fila.get(ubicacion_1[0].upper())-1
                ubicacion_2 = input('Ubicacion 2: elija la fila (A..E) seguido de un numero (1..5? ? ')
                x2 = equiv_fila.get(ubicacion_2[0].upper())-1
                y = int(ubicacion_1[1]) - 1
                print(f'Su nave ocupara las posiciones : {ubicacion_1[0].upper()}{y+1} y {ubicacion_2[0].upper()}{y+1}')
                mat[x1][y] = nave
                mat[x2][y] = nave
    print('--------------------------------------------\n\n')
    pprint.pprint(mat)

def cuenta_naves(mat):
    count = 0
    for y in range(5):
        for x in range(5):
            if mat[x][y] == 1 or mat[x][y] == 2:
                count += 1
    return count
    
  
inicio()
jugar()







