from estado import Estado
from posicion import Posicion

class Nodo:
    def __init__(self):
        self.estado = Estado()
        self.padre = None
        self.solucion = ''
        self.operadorAplicado = ''
        self.profundidad = 0
        self.moviCaja = False
        self.posPuntosLLegada = []
        
    def esMeta(self):
        for punto in self.posPuntosLLegada:
            for index,caja in enumerate(self.estado.posCajas):
                if(punto.x == caja.x and punto.y == caja.y):
                    break
                if(index == len(self.estado.posCajas)-1):
                    return False
        return True

    #metodos que facilitan la creacion de nodos de acuerdo a las reglas del juego

    #retorna verdadero o falso si sobre la posicion pasada se encuentra una caja
    def hayCaja(self,posicion):
        hay_Caja = False
        for caja in self.estado.posCajas:
            if(posicion.x == caja.x and posicion.y == caja.y):
                hay_Caja = True
        return hay_Caja
    
    def hayMuro(self,posicion):
        return self.estado.tablero[posicion.x][posicion.y] == 'W'

    #actualiza la posicion de una caja para un nuevo nodo retornando la lista de cajas (por valor)
    def actualizarCaja(self, posicionActual, nuevaPosicion):
        cajas = self.estado.posCajas[:]
        nuevasCajas = []
        for caja in cajas:
            if(caja.x == posicionActual.x and caja.y == posicionActual.y):
                aux = Posicion.positionGiven(nuevaPosicion.x, nuevaPosicion.y)
                nuevasCajas.append(aux)
            else:
                nuevasCajas.append(caja)
        return nuevasCajas
    
    def crearNodo(self,posicionAlmacenista,operador,moviCaja = False,posicionCaja = False):

        nuevaPosicion = posicionAlmacenista

        estado = Estado()
        estado.tablero = self.estado.tablero
        estado.posAlmacenista = nuevaPosicion 
        if(posicionCaja != False):
            estado.posCajas = self.actualizarCaja(posicionAlmacenista,posicionCaja)
        else:
            estado.posCajas = self.estado.posCajas[:]

        nodo = Nodo()
        nodo.estado = estado
        nodo.solucion = self.solucion + operador
        nodo.moviCaja = moviCaja
        nodo.profundidad = self.profundidad + 1
        nodo.padre = self
        nodo.operadorAplicado = operador
        nodo.posPuntosLLegada = self.posPuntosLLegada

        return nodo

    def crearNodoOperador(self,nuevaPosicion,operador, nuevaPosicionCaja):
        if(not(self.hayMuro(nuevaPosicion))):
            if(self.hayCaja(nuevaPosicion)):
                if(not(self.hayMuro(nuevaPosicionCaja)) and not(self.hayCaja(nuevaPosicionCaja))):
                    return self.crearNodo(nuevaPosicion,operador,True,nuevaPosicionCaja)
            else:
                return (self.crearNodo(nuevaPosicion,operador))
        return None

    def crearNodos(self):
        nodos = []
        pos = self.estado.posAlmacenista
    
        nodos.append(self.crearNodoOperador(Posicion.positionGiven(pos.x-1,pos.y),'U',Posicion.positionGiven(pos.x-1-1,pos.y)))
        nodos.append(self.crearNodoOperador(Posicion.positionGiven(pos.x+1,pos.y),'D',Posicion.positionGiven(pos.x+1+1,pos.y)))
        nodos.append(self.crearNodoOperador(Posicion.positionGiven(pos.x,pos.y-1),'L',Posicion.positionGiven(pos.x,pos.y-1-1)))   
        nodos.append(self.crearNodoOperador(Posicion.positionGiven(pos.x,pos.y+1),'R',Posicion.positionGiven(pos.x,pos.y+1+1)))

        aux = []
        for nodo in nodos:
            if not(nodo is None):
                aux.append(nodo) 
        return aux
