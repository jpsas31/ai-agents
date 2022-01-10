from estado import Estado
from posicion import Posicion

class Nodo:
    def __init__(self):
        self.estado = Estado()
        self.padre = None
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

    def solucion(self):
        if(self.padre is None):
            return ''
        return self.operadorAplicado+self.padre.solucion()

    #metodos que facilitan la creacion de nodos de acuerdo a las reglas del juego

    #retorna verdadero o falso si sobre la posicion pasada se encuentra una caja
    def hayCaja(self,x,y):
        hay_Caja = False
        for caja in self.estado.posCajas:
            if(x == caja.x and y == caja.y):
                hay_Caja = True
        return hay_Caja

    #actualiza la posicion de una caja para un nuevo nodo retornando la lista de cajas
    def actualizarCaja(self, x, y, nx, ny):
        cajas = self.estado.posCajas[:]
        nuevasCajas = []
        for caja in cajas:
            if(caja.x == x and caja.y == y):
                aux = Posicion()
                aux.x = nx
                aux.y = ny
                nuevasCajas.append(aux)
            else:
                nuevasCajas.append(caja)
        return nuevasCajas
    
    def hayMuro(self,x,y):
        return self.estado.tablero[x][y] == 'W'

    def crearNodo(self,x,y,operador,moviCaja = False,cx = False,cy = False):

        nuevaPosicion = Posicion()
        nuevaPosicion.x = x
        nuevaPosicion.y = y

        estado = Estado()
        estado.tablero = self.estado.tablero
        estado.posAlmacenista = nuevaPosicion 
        if(cx != False and cy != False):
            estado.posCajas = self.actualizarCaja(x,y,cx,cy)
        else:
            estado.posCajas = self.estado.posCajas[:]

        nodo = Nodo()
        nodo.estado = estado
        nodo.moviCaja = moviCaja
        nodo.profundidad = self.profundidad + 1
        nodo.padre = self
        nodo.operadorAplicado = operador
        nodo.posPuntosLLegada = self.posPuntosLLegada

        return nodo

    def crearNodoOperador(self,x,y,operador, direccionx = 0, direcciony = 0):
        if(not(self.hayMuro(x,y))):
            if(self.hayCaja(x,y)):
                if(not(self.hayMuro(x+direccionx,y+direcciony)) and not(self.hayCaja(x+direccionx,y+direcciony))):
                    return self.crearNodo(x,y,operador,True,x+direccionx,y+direcciony)
            else:
                return (self.crearNodo(x,y,operador))
        return None

    def crearNodos(self):
        nodos = []
        pos = self.estado.posAlmacenista
        
        if(self.operadorAplicado != 'D' or self.moviCaja):
            nodos.append(self.crearNodoOperador(pos.x-1, pos.y,'U',-1,0))
        if(self.operadorAplicado != 'U' or self.moviCaja):
            nodos.append(self.crearNodoOperador(pos.x+1, pos.y,'D',1,0))  
        if(self.operadorAplicado != 'R' or self.moviCaja):
            nodos.append(self.crearNodoOperador(pos.x, pos.y-1,'L',0,-1))     
        if(self.operadorAplicado != 'L' or self.moviCaja):
            nodos.append(self.crearNodoOperador(pos.x, pos.y+1,'R',0,1))

        aux = []
        for nodo in nodos:
            if not(nodo is None):
                aux.append(nodo)
        
        return aux