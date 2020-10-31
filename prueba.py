
import os

class Nodo:
    def __init__(cuadro, posicion, padre, movimiento, profundidad, correctos):        
        cuadro.posicion = posicion                      
        cuadro.padre = padre                         
        cuadro.movimiento = movimiento                
        cuadro.profundidad = profundidad              
        cuadro.correctos = correctos    

    def movimientos(cuadro, direccion):
        posicion = list(cuadro.posicion)
        indice = posicion.index(0)

        if direccion == "1":            
            if indice not in [6, 7, 8]:                
                temp = posicion[indice + 3]
                posicion[indice + 3] = posicion[indice]
                posicion[indice] = temp
                return tuple(posicion)
            else:                
                return None

        elif direccion == "2":            
            if indice not in [0, 1, 2]:                
                temp = posicion[indice - 3]
                posicion[indice - 3] = posicion[indice]
                posicion[indice] = temp
                return tuple(posicion)
            else:                
                return None

        elif direccion == "3":            
            if indice not in [0, 3, 6]:                
                temp = posicion[indice - 1]
                posicion[indice - 1] = posicion[indice]
                posicion[indice] = temp
                return tuple(posicion)
            else:                
                return None

        elif direccion == "4":            
            if indice not in [2, 5, 8]:                
                temp = posicion[indice + 1]
                posicion[indice + 1] = posicion[indice]
                posicion[indice] = temp
                return tuple(posicion)
            else:                
                return None        
    def encontrar_sucesores(cuadro):
        sucesores = []
        hijo1 = cuadro.movimientos("1")
        hijo2 = cuadro.movimientos("2")
        hijo3 = cuadro.movimientos("3")
        hijo4 = cuadro.movimientos("4")
        
        sucesores.append(Nodo(hijo1, cuadro, "1", cuadro.profundidad + 1, h(hijo1)))
        sucesores.append(Nodo(hijo2, cuadro, "2", cuadro.profundidad + 1, h(hijo2)))
        sucesores.append(Nodo(hijo3, cuadro, "3", cuadro.profundidad + 1, h(hijo3)))
        sucesores.append(Nodo(hijo4, cuadro, "4", cuadro.profundidad + 1, h(hijo4)))
        
        sucesores = [nodo for nodo in sucesores if nodo.posicion != None]  
        return sucesores

    def encontrar_camino(cuadro, puzzle):
        camino = []
        nodo_actual = cuadro
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    def imprimir_nodo(cuadro):
        renglon = 0
        for pieza in cuadro.posicion:
            if pieza == 0:
                print(" ", end = " ")
            else:
                print (pieza, end = " ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0       

def h(posicion):
    correcto = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    valor_correcto = 0
    correctos = 0
    if posicion:
        for valor_pieza, valor_correcto in zip(posicion, correcto):
            if valor_pieza == valor_correcto:
                correctos += 1
            valor_correcto += 1
    return correctos   

def Funcion_HillClimbing(puzzle):
    visitados = set()  
    nodo_actual = Nodo(puzzle, None, None, 0, h(puzzle))

    while nodo_actual.correctos < 9:             
        sucesores = nodo_actual.encontrar_sucesores()   
        max_correctos = -1
        for nodo in sucesores:   
            if nodo.correctos >= max_correctos and nodo not in visitados:
                max_correctos = nodo.correctos
                nodo_siguiente = nodo

            visitados.add(nodo_actual)
        if nodo_siguiente.correctos >= nodo_actual.correctos:
            nodo_actual = nodo_siguiente
        else:
            print("\n Maximo local")
            break
    else:
        print("\n¡Se encontró la meta!")        
    return nodo_actual.encontrar_camino(puzzle)

def main():
    posicion_final = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    posicion_inicial = (1, 2, 3, 0, 5, 6, 4, 7, 8)
    print("posicion inicial:")
    (Nodo(posicion_inicial, None, None, 0, h(posicion_inicial))).imprimir_nodo()
    print("\t Hill Climbing")
    nodos_camino = Funcion_HillClimbing(posicion_inicial)
 
    if nodos_camino:      
            for nodo in nodos_camino:
                nodo.imprimir_nodo()
                print("\nPiezas correctas:", nodo.correctos, "\n")     
    else:
        print ("\nNo se encontró un camino con las condiciones dadas.")

    return 0    

if __name__ == "__main__":
    main()

    