from tp import Pile

n = 5
plateau = [ [-1 for i in range(n)]
           for j in range(n)]
deplacements = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]

def est_dans(pos):
    """ (int, int) -> bool """
    x, y = pos
    return 0 <= x < n and 0 <= y < n

def est_visitee(pos):
    """ (int, int) -> bool
    Détermine si la position pos = (x, y) a déjà été visitée """
    x, y = pos
    if plateau[x][y] == -1:
        return False
    return True

def a_partir_de(pos):
    """ (int, int) -> Pile
    Renvoie une pile constituée des éléments accessibles depuis pos
    avec l'état courant du plateau. '"""
    p = Pile()
    for d in deplacements:
        n_pos = (d[0] + pos[0], d[1] + pos[1])
        if est_dans(n_pos) and not est_visitee(n_pos):
            p.empiler(n_pos)
    return p

        
        
        
        
        
        

