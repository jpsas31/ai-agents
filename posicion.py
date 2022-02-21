# Representa una posicion en el plano cartesiano
# posee un constructor (position_given)
# el metodo __repr__ representa el objeto como cadena de la forma x-y
# el metodo __eq__ determina si una posicion es igual a otra
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
    
    def __eq__(self, other):
        if(type(other) != type(self)):
            return False

        return ((self.x == other.x) and (self.y == other.y))
    