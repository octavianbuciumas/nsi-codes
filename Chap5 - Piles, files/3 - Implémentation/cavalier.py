from tp import Pile

n = 8
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

def cavalier():
    """ () -> Pile
    Renvoie une pile constituée des mouvements à effectuer pour
    obtenir un chemin de cavalier passant par toutes les cases du plateau. """

    pos = (0,0)
    # le sommet de la pile parcours contient
    # la position courante
    pile_parcours = Pile()
    pile_parcours.empiler(pos)
    # initialement le chemin est de longueur 1
    longueur_chemin = 1
    # le sommet de la pile essais contient
    # les positions à explorer à partir de la position courante
    pile_essais = Pile()
    pile_essais.empiler(a_partir_de(pos))
    # on indique la position courante comme visitée
    plateau[pos[0]][pos[1]] = 1
    while longueur_chemin < n**2:
        # on récupère l'état courant du cavalier :
        # sa position se trouve au sommet de la pile parcours
        # et ses mouvements à explorer au sommet de la pile essais
        pos = pile_parcours.sommet.valeur
        accessibles = pile_essais.sommet.valeur
        # Dans le cas où il est possible de visiter une
        # case à partir de la position courante
        if not accessibles.est_vide() :
            # on choisit la première position à explorer
            # il ne sera plus nécessaire de l'explorer
            # par la suite, on la supprime de accessibles
            pos = accessibles.depiler()
            # on indique que la case pos a été visitée
            plateau[pos[0]][pos[1]] = 1 
            longueur_chemin += 1
            # on met à jour les piles de parcours et d'essais
            pile_parcours.empiler(pos)
            pile_essais.empiler(a_partir_de(pos))
        else:
            # la position courante est un cul de sac
            # on met à jour le plateau (la case courante
            # redevient accessible)
            plateau[pos[0]][pos[1]] = -1
            # on revient à la dernière configuration connue qui
            # ne menait pas à un cul de sac en dépilant les piles
            # parcours et essais
            pos = pile_parcours.depiler()
            pile_essais.depiler()
            # on met à jour la longueur du chemin
            longueur_chemin -= 1
        # si jamais la pile du parcours est vide
        # c'est qu'il n'y a pas de solution au problème
        if pile_parcours.est_vide():
            raise IndexError("Pas de solution trouvée au problème")
    return pile_parcours

        
        
        

