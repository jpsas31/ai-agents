class Posicion:
    def __init__(self):
        self.x = -1
        self.y = -1
    
    @classmethod
    def position_given(cls, x, y):
        aux = cls()
        aux.x = x
        aux.y = y
        return aux

    def __repr__(self):
        return str(self.x)+'-'+str(self.y)
        