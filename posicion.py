class Posicion:
    def __init__(self):
        self.x = -1
        self.y = -1
    
    @classmethod
    def positionGiven(cls, x, y):
        aux = cls()
        aux.x = x
        aux.y = y
        return aux
