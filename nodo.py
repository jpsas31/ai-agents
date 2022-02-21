from estado import Estado
from posicion import Posicion

# Representa un nodo en el arbol formado por:
#   estado ver clase Estado
#   padre referencia a otro Nodo
#   la solucion que se va construyendo
#   la profundidad en la que se encuentra en el nodo
#   operador_aplicado para llegar a este nodo
#   tablero mapa del mundo

# Funciones
#   la función es_meta determina si el nodo actual es meta
#   la funcion hay_caja determina si para una posicion (a la que se quiere mover el almacenista) existe una caja, retorna falso o verdadero
#   la funcion hay_muro determina si para una posicion (a la que se quiere mover el almacenista) existe un muro, retorna falso o verdadero
#   la función actualizar_cajas copia la lista de cajas de un estado, y actualiza de ser necesario la caja que se quiera mover
#   la funcion crear_nodo crea un nodo nuevo tomando la posicion nueva a la que se quiere mover
#   la funcion puedo_crear_nodo revisa que la posicion a la que queramos movernos cumpla las reglas del juego
#   la funcion crear_nodos crea una lista de nodos ordenados por prioridad de UDLR en caso de que se pueda mover a esa decision 
class Nodo:
    def __init__(self):
        self.estado = Estado()
        self.padre = None
        self.solucion = ''
        self.profundidad = 0
        self.operador_aplicado = ''
        self.tablero = []

    def es_meta(self):
        for caja in self.estado.pos_cajas:
            if(self.tablero[caja.x][caja.y] != 'X'):
                return False
        return True

    def hay_caja(self,posicion):
        for posCaja in self.estado.pos_cajas:
            if(posCaja == posicion):
                return True
        return False

    def hay_muro(self,posicion):
        return self.tablero[posicion.x][posicion.y] == 'W'

    def actualizar_cajas(self, posicion_actual = False, nueva_posicion = False):
        cajas = self.estado.pos_cajas[:]
        if(not(nueva_posicion)):
            return cajas
        
        for index,caja in enumerate(cajas):
            if(caja == posicion_actual):
                cajas.pop(index)
                cajas.insert(index, Posicion.position_given(nueva_posicion.x, nueva_posicion.y))
        return cajas
        
    def crear_nodo(self,posicion_almacenista,operador,posicion_caja = False):
        nodo = Nodo()
        estado = Estado()

        estado.pos_almacenista = posicion_almacenista
        estado.pos_cajas = self.actualizar_cajas(posicion_almacenista,posicion_caja)

        nodo.estado = estado
        nodo.padre = self
        nodo.tablero = self.tablero
        nodo.solucion = self.solucion + operador
        nodo.profundidad = self.profundidad + 1
        nodo.operador_aplicado = operador
        return nodo

    def puedo_crear_nodo(self,nueva_posicion,operador, nueva_posicion_caja):
        if(not(self.hay_muro(nueva_posicion))):
            if(self.hay_caja(nueva_posicion)):
                if(not(self.hay_muro(nueva_posicion_caja)) and not(self.hay_caja(nueva_posicion_caja))):
                    return self.crear_nodo(nueva_posicion,operador,nueva_posicion_caja)
            else:
                return self.crear_nodo(nueva_posicion,operador)
        return None

    def crear_nodos(self):
        nodos = []
        pos = self.estado.pos_almacenista    

        arriba = self.puedo_crear_nodo(Posicion.position_given(pos.x-1,pos.y),'U',Posicion.position_given(pos.x-2,pos.y))
        abajo = self.puedo_crear_nodo(Posicion.position_given(pos.x+1,pos.y),'D',Posicion.position_given(pos.x+2,pos.y))
        izquierda = self.puedo_crear_nodo(Posicion.position_given(pos.x,pos.y-1),'L',Posicion.position_given(pos.x,pos.y-2))
        derecha = self.puedo_crear_nodo(Posicion.position_given(pos.x,pos.y+1),'R',Posicion.position_given(pos.x,pos.y+2))

        nodos.append(arriba) if arriba is not None else 1
        nodos.append(abajo) if abajo is not None else 1
        nodos.append(izquierda) if izquierda is not None else 1
        nodos.append(derecha) if derecha is not None else 1
    
        return nodos
