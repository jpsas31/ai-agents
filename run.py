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
        nodo_raiz.tablero.append(linea)
    else:
        if(nodo_raiz.estado.pos_almacenista.x == -1):
            nodo_raiz.estado.pos_almacenista = Posicion.position_given(int(linea[0]),int(linea[2])) 
        else:
            nodo_raiz.estado.pos_cajas.append(Posicion.position_given(int(linea[0]), int(linea[2])))


def amplitud(nodo_raiz):
    cola = []
    cola.append(nodo_raiz)
    while(True):
        if(len(cola) == 0):
            return None
        
        nodo = cola.pop(0)
        
        if(nodo.profundidad > 64):
            return None
        
        if(nodo.es_meta()):
            return nodo.solucion
        else:
            cola.extend(nodo.crear_nodos())

        
def profundidad(nodo_raiz, profundidad):
    pila = []
    pila.append(nodo_raiz)
    while(True):
        if(len(pila) == 0):
            return None
        
        nodo = pila.pop()
       
        if(nodo.es_meta()):
            return nodo.solucion
        else:
            if(nodo.profundidad < profundidad):
                pila.extend(nodo.crear_nodos()) # aqui se deben reordenar los nodos para que tenga prioridad de acuerdo al orden que planteo el profesor antes
                                                # de añadirlos a la pila


def profundidad_iterativa(nodo_raiz):
    profundidad_inicial = 10
    while(True):
        if(profundidad_inicial > 64):
            return None

        nodo_raiz.mundo = {}
        res = profundidad(nodo_raiz, profundidad_inicial)
        
        if(res is None):
            profundidad_inicial += 1
        else:
            return res

#print(amplitud(nodo_raiz))

# print(profundidad(nodo_raiz, 64))

# print(profundidad_iterativa(nodo_raiz))
