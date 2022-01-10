from nodo import Nodo
from posicion import Posicion


archivo = open('nivel1.txt')
nodoraiz = Nodo()
for linea in archivo:

#inicio del script

# while(True):
#     try:
#         linea = input()
#     except:
#           break  
    if(linea.find(',') == -1):
        nodoraiz.estado.tablero.append(linea)
    else:
        if(nodoraiz.estado.posAlmacenista.x == -1):
            nodoraiz.estado.posAlmacenista.x = int(linea[0])
            nodoraiz.estado.posAlmacenista.y = int(linea[2])
        else:
            aux = Posicion()
            aux.x = int(linea[0])
            aux.y = int(linea[2])
            nodoraiz.estado.posCajas.append(aux)

for index,linea in enumerate(nodoraiz.estado.tablero):
    for pos, caracter in enumerate(linea):
        if(caracter == 'X'):
            aux = Posicion()
            aux.x = index
            aux.y = pos
            nodoraiz.posPuntosLLegada.append(aux)
            
#amplitud
cola = []
cola.append(nodoraiz)

for index, nodo in enumerate(cola):
    if(nodo.profundidad == 10):
        continue
    if(nodo.esMeta()):
        print(nodo.solucion())
        break
    else:
        cola.extend(nodo.crearNodos())

#profundidad
# pila = []
# cola.append(nodoraiz)

# for index,nodo in enumerate(pila):
