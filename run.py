from nodo import Nodo
from posicion import Posicion


nodo_raiz = Nodo()
# while(True):
#     try:
#         linea = input()
#     except:
#           break
archivo = open('nivel1.txt')
for linea in archivo:

    if(linea.find(',') == -1):
        nodo_raiz.estado.tablero.append(linea)
    else:
        if(nodo_raiz.estado.pos_almacenista.x == -1):
            nodo_raiz.estado.pos_almacenista = Posicion.position_given(int(linea[0]),int(linea[2])) 
        else:
            nodo_raiz.estado.pos_cajas.append(Posicion.position_given(int(linea[0]), int(linea[2])))


def amplitud(nodo_raiz):
    cola = []
    cola.append(nodo_raiz)
    while(True):
        nodo = cola.pop(0)
        if(nodo.es_meta()):
            print(nodo.solucion)
            break
        else:
            cola.extend(nodo.crear_nodos())

        
def profundidad(nodo_raiz):
    pila = []
    pila.append(nodo_raiz)
    while(True):
        if(len(pila) == 0):
            break
        nodo = pila.pop()
        if(nodo.profundidad == 64):
            continue
        if(nodo.es_meta()):
            print(nodo.solucion)
            break
        else:
            pila.extend(nodo.crear_nodos())


def profundidad_iterativa(nodo_raiz):
    pila = []
    pila.append(nodo_raiz)
    iterador = 10
    while(True):
        if(len(pila) == 0):
            iterador += 1
            break
        nodo = pila.pop()
        if(nodo.profundidad == iterador):
            continue
        if(nodo.es_meta()):
            print(nodo.solucion)
            break
        else:
            pila.extend(nodo.crear_nodos())
    if(iterador != 64):
        nodo_raiz.mundo = {}
        profundidad_iterativa(nodo_raiz)

amplitud(nodo_raiz)
nodo_raiz.mundo = {}
profundidad(nodo_raiz)
nodo_raiz.mundo = {}
profundidad_iterativa(nodo_raiz)
