from posicion import Posicion

# Representa un estado del juego formado por la posicion del almacenista y una lista
# de la posicion de las cajas
# el metodo __eq__ permite determinar si dos estados son iguales
# el metodo __repr__ permite mostrar un objeto estado como cadena como patron pos-almacenista;pos-cajas...

class Estado:
    def __init__(self):
        self.pos_almacenista = Posicion()  
        self.pos_cajas = []

    def __eq__(self, other):
        if(type(other) != type(self)):
            return False
        
        if(len(self.pos_cajas) != len(other.pos_cajas)):
            return False

        valor = True

        for index,pos_caja in enumerate(self.pos_cajas):
            if(pos_caja != other.pos_cajas[index]):
                valor = False
                break

        return ((self.pos_almacenista == other.pos_almacenista) and valor )

    def __repr__(self):

        valor = str(self.pos_almacenista)+';'

        for pos_caja in self.pos_cajas:
            valor += str(pos_caja)

        return valor