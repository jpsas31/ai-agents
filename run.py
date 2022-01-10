from nodo import Nodo
from posicion import Posicion


archivo = open('nivel1.txt')
nodoraiz = Nodo()
for linea in archivo:
    # print(linea)
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
# cola = []
# cola.append(nodoraiz)
# while(True):
#     nodo = cola.pop(0)
#     if(nodo.esMeta()):
#         print(nodo.getSolucion())
#         break
#     else:
#         cola.extend(nodo.crearNodos())

# print("salio")

        
#profundo
pila = []
pila.append(nodoraiz)
while(True):
    nodo = pila.pop()
    print(nodo.profundidad)
  

    if(nodo.esMeta()):
        print(nodo.getSolucion())
        break
    else:
        if(nodo.profundidad== 30): continue
        pila.extend(nodo.crearNodos())
