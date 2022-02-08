from re import I
from nodo import Nodo
from posicion import Posicion
from ciclos import quitar_ciclos

nodo_raiz = Nodo()

# while(True):
#     try:
#         linea = input()
#     except:
#           break
archivo = open('niveles/nivel4.txt')
for linea in archivo:

    if(linea.find(',') == -1):
        nodo_raiz.tablero.append(linea)
    else:
        if(nodo_raiz.estado.pos_almacenista.x == -1):
            nodo_raiz.estado.pos_almacenista = Posicion.position_given(int(linea[0]),int(linea[2])) 
        else:
            nodo_raiz.estado.pos_cajas.append(Posicion.position_given(int(linea[0]), int(linea[2])))


def amplitud(nodo_raiz):
    almacen = {}
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

        nodos = nodo.crear_nodos()

        for nodo_anadir in nodos:
            estado = str(nodo_anadir.estado)
            
            if(not(almacen.get(estado)) or (almacen.get(estado) and (nodo_anadir.profundidad < almacen.get(estado).profundidad))):
                almacen.update({estado: nodo_anadir })
                cola.append(nodo_anadir)
                

        
def profundidad(nodo_raiz, profundidad):
    almacen = {}
    pila = []
    pila.append(nodo_raiz)
    while(True):
        if(len(pila) == 0):
            return None
        
        nodo = pila.pop()
       
        if(nodo.es_meta()):
            return nodo.solucion

        if(nodo.profundidad < profundidad):
            
            nodos = nodo.crear_nodos()

            for nodo_anadir in nodos:
                estado = str(nodo_anadir.estado)
                
                if(not(almacen.get(estado)) or (almacen.get(estado) and (nodo_anadir.profundidad < almacen.get(estado).profundidad))):
                    almacen.update({estado: nodo_anadir })
                    pila.append(nodo_anadir)


def profundidad_iterativa(nodo_raiz):
    profundidad_inicial = 10
    while(True):
        if(profundidad_inicial > 64):
            return None

        nodo_raiz.mundo = {}
        res = profundidad(nodo_raiz, profundidad_inicial)
        
        if(res is not None):
            return res
        
        profundidad_inicial += 1
        
print(amplitud(nodo_raiz))

print(profundidad(nodo_raiz, 64))

print(profundidad_iterativa(nodo_raiz))
