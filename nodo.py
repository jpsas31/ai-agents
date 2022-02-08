from estado import Estado
from posicion import Posicion

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
