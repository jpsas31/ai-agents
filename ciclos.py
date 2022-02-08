def quitar_ciclos(nodos,profundidad):
    optimizado = []

    for nodo in nodos:
       if(not(tiene_ciclo(nodo.padre, nodo.estado, profundidad))):
           optimizado.append(nodo)

    return optimizado

def tiene_ciclo(padre, estado, profundidad):
    if(padre == None):
        return False
        
    if(profundidad == 0):
        return False

    return True if padre.estado == estado else tiene_ciclo(padre.padre, estado, --profundidad)


