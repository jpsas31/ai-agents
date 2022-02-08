from posicion import Posicion

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

        for index,posCaja in enumerate(self.pos_cajas):
            if(posCaja != other.pos_cajas[index]):
                valor = False
                break

        return ((self.pos_almacenista == other.pos_almacenista) and valor )
