from ds import *

def existe_chemin(G, sommet, destination):
    """ Graphe, Sommet, Sommet -> bool
    Renvoie True si et seulement si il existe un chemin entre source et destination dans G. """
    # il suffit de parcourir le graphe depuis
    # sommet : si on trouve destination c'est bon
    ordre_vus = parcours_profondeur(G, sommet)
    return destination in ordre_vus
    # ordre_vus est ici une liste

def composantes_connexes(G):
    """ Graphe -> {Sommet:int}
    Détermine les composantes connexes du graphe G sous la forme d'un dictionnaire """
    composantes = {cle:None for cle in G.sommets()}
    num_composante = 0
    for s in G.sommets():
        # if composantes[s] != None:
        #    continue
        if composantes[s] == None:
            atteignables = parcours_profondeur(G, s)
            for atteignable in atteignables:
                composantes[atteignable] = num_composante
            num_composante += 1
    return composantes
    
BLANC, GRIS, NOIR = 0, 1, 2

def parcours_cycle(G, depart, couleurs):
    """ Graphe, Sommet, {Sommet:Couleur} -> bool
    Renvoie True si et seulement si  il existe un cycle dans le graphe G dans la composante connexe de depart. 
    On suppose que depart est en BLANC. """
    couleurs[depart] = GRIS
    # début du parcours récursif
    for destination in G.voisins(depart):
        if couleurs[destination] == BLANC:
            return parcours_cycle(G, destination, couleurs)
            # renvoie vrai si on trouve un cycle
            # en parcourant le graphe depuis
            # destination
        elif couleurs[destination] == GRIS:
            return True
    # fin du parcours récursif
    couleurs[depart] = NOIR
    return False

def contient_cycle(G):
    """ Graphe -> bool
    Renvoie True ssi le graphe orienté G contient un cycle """
    couleurs = {s:0 for s in G.sommets()}
    for s in G.sommets():
        if not couleurs == NOIR:
            rep = parcours_cycle(G, s, couleurs)
            # return rep == True ne fonctionne pas
            # on veut continuer dans le cas ou rep
            # est False
            if rep == True:
                return True
    return False

def distance(G, depart, arrivee):
    """ Graphe, Sommet, Sommet -> int 
    Renvoie la longueur du plus petit chemin entre depart et arrivee dans G """
    pass

def diametre(G):
    """ Graphe -> int
    Renvoie la distance maximale entre deux sommets quelconques du graphe """
    pass

