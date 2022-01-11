from estado import Estado
from posicion import Posicion

class Nodo:
    def __init__(self):
        self.estado = Estado()
        self.padre = None
        self.solucion = ''
        self.profundidad = 0
        self.mundo = {}
        
    def es_meta(self):
        for caja in self.estado.pos_cajas:
            if(self.estado.tablero[caja.x][caja.y] != 'X'):
                return False
        return True

    #metodos que facilitan la creacion de nodos de acuerdo a las reglas del juego

    #retorna verdadero o falso si sobre la posicion pasada se encuentra una caja
    def hay_caja(self,posicion):
        for caja in self.estado.pos_cajas:
            if(posicion.x == caja.x and posicion.y == caja.y):
                return True
        return False
    
    def hay_muro(self,posicion):
        return self.estado.tablero[posicion.x][posicion.y] == 'W'

    #actualiza la posicion de una caja para un nuevo nodo retornando la lista de cajas (por valor)
    def actualizar_caja(self, posicion_actual = False, nueva_posicion = False):
        cajas = self.estado.pos_cajas[:]
        nuevas_cajas = []
        for caja in cajas:
            if(caja.x == posicion_actual.x and caja.y == posicion_actual.y):
                aux = Posicion.position_given(nueva_posicion.x, nueva_posicion.y)
                nuevas_cajas.append(aux)
            else:
                nuevas_cajas.append(caja)
        return nuevas_cajas
    
    def crear_nodo(self,posicion_almacenista,operador,posicion_caja = False):
        nodo = Nodo()
        estado = Estado()

        estado.tablero = self.estado.tablero
        estado.pos_almacenista = posicion_almacenista

        if(posicion_caja != False):
            estado.pos_cajas = self.actualizar_caja(posicion_almacenista,posicion_caja)
        else:
            estado.pos_cajas = self.estado.pos_cajas[:]
            nodo.mundo = self.mundo

        nodo.estado = estado
        nodo.padre = self
        nodo.solucion = self.solucion + operador
        nodo.profundidad = self.profundidad + 1
        return nodo

    def puedo_crear_nodo(self,nueva_posicion,operador, nueva_posicion_caja):
        if(self.mundo.get(str(nueva_posicion)) == True):
            return None
        if(not(self.hay_muro(nueva_posicion))):
            if(self.hay_caja(nueva_posicion)):
                if(not(self.hay_muro(nueva_posicion_caja)) and not(self.hay_caja(nueva_posicion_caja))):
                    return self.crear_nodo(nueva_posicion,operador,nueva_posicion_caja)
            else:
                return (self.crear_nodo(nueva_posicion,operador))
        return None

    def crear_nodos(self):
        nodos = []
        pos = self.estado.pos_almacenista    
        self.mundo[str(self.estado.pos_almacenista)] = True

        nodos.append(self.puedo_crear_nodo(Posicion.position_given(pos.x-1,pos.y),'U',Posicion.position_given(pos.x-1-1,pos.y)))
        nodos.append(self.puedo_crear_nodo(Posicion.position_given(pos.x+1,pos.y),'D',Posicion.position_given(pos.x+1+1,pos.y)))
        nodos.append(self.puedo_crear_nodo(Posicion.position_given(pos.x,pos.y-1),'L',Posicion.position_given(pos.x,pos.y-1-1)))   
        nodos.append(self.puedo_crear_nodo(Posicion.position_given(pos.x,pos.y+1),'R',Posicion.position_given(pos.x,pos.y+1+1)))

        aux = []
        for nodo in nodos:
            if not(nodo is None):
                aux.append(nodo) 
        return aux
