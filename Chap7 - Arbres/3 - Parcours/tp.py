from ds import *

a = Arbre("Kamel",
          Arbre("Kamel",
                Arbre("Joris", None, None),
                Arbre("Kamel", None, None)),
          Arbre("Carine",
                Arbre("Carine", None, None),
                Arbre("Abdou", None, None)))


def nb_joueurs(a):
    """ Arbre -> int
    Renvoie le nombre de joueurs ayant participé à la compétition d'arbre a """
    # en fait c'est le nombre de feuilles
    if est_feuille(a):
        return 1
    # l'arbre est supposé parfait : pas besoin de ça ici
    # elif est_vide(gauche(a)):
    #    return nb_joueurs(droit(a))
    # elif est_vide(droit(a)):
    #    return nb_joueur(gauche(a))
    else:
        return nb_joueurs(gauche(a)) + nb_joueurs(droit(a))

def nb_rounds(a):
    """ Arbre -> int
    Renvoie le nombre de rounds de la compétition a """
    # en fait c'est la hauteur
    if est_feuille(a):
        return 0
    else:
        # ça marche car les arbres sont parfaits
        ag = nb_rounds(gauche(a))
        return ag + 1 
        # ad = nb_rounds(droit(a))
        # return max(ag, ad) + 1 

def occurrences(a, nom):
    """ Arbre, str -> int
    Renvoie le nombre d'occurrences de nom dans a """
    if est_vide(a):
        return 0
    else:
        if etiquette(a) == nom:
            return 1 + occurrences(gauche(a), nom) + occurrences(droit(a), nom)
        else:
            return occurrences(gauche(a), nom) + occurrences(droit(a), nom)

def nombre_matchs(a, nom):
    """ Arbre, str -> int
    Renvoie le nombre de matchs joués par le joueur nom dans la compétition d'arbre a """
    return  occurrences(a, nom) - 1 if etiquette(a) == nom else occurrences(a, nom)
    # if etiquette(a) == nom:
    #     return occurrences(a, nom) - 1
    # else:
    #     return occurrences(a, nom)

def liste_joueurs(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant participé à la compétition d'arbre a """
    if est_vide(a):
        return []
    elif est_feuille(a):
        return [etiquette(a)]
    else:
        return liste_joueurs(gauche(a)) + liste_joueurs(droit(a))
    
def liste_joueurs2(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant participé à la compétition d'arbre a """
    if est_vide(a):
        return []
    elif est_feuille(a):
        return [etiquette(a)]
    else:
        l = liste_joueurs2(gauche(a))
        l.extend(liste_joueurs2(droit(a)))
        return l
    
def niveau(a, i):
    """ Arbre, int -> [str]
    Renvoie la liste des étiquettes des nœuds de profondeur i de l'arbre a """
    if i == 0:
        return [etiquette(a)]
    else:
        ag = niveau(gauche(a), i - 1)
        ad  = niveau(droit(a), i -1)
        return ag + ad # + concatène les listes

def vaincus_gagnant(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant joué un match contre le gagnant de la compétition d'arbre a """
    if est_vide(a):
        return []
    elif est_feuille(a):
        return []
    else:
        ag = vaincus_gagnant(gauche(a))
        ad = vaincus_gagnant(droit(a))
        if etiquette(a) == etiquette(gauche(a)):
            return ag + [etiquette(droit(a))]
        else:
            return ad + [etiquette(gauche(a))]
        
def parcours_largeur(a):
    """ Arbre -> [str]
    Renvoie la liste des étiquettes des nœuds de l'arbre a, telle qu'obtenue à l'aide d'un parcours en largeur """
    file = [a]
    liste_vus = []
    while not file == []:
        n = file[0]
        liste_vus.append(etiquette(n))
        file.pop(0)
        if not est_vide(gauche(n)):
            file.append(gauche(n))
        if not est_vide(droit(n)):
            file.append(droit(n))
    return liste_vus

def recherche_noeud(a, nom):
    """ Arbre, str -> Arbre
    Renvoie le sous-arbre de a dont la racine a pour étiquette nom et est de profondeur minimale dans a """
    file = [a]
    liste_vus = []
    while not file == []:
        n = file[0]
        # opération de traitement :
        if etiquette(n) == nom:
            return n 
        file.pop(0)
        if not est_vide(gauche(n)):
            file.append(gauche(n))
        if not est_vide(droit(n)):
            file.append(droit(n))

def joueurs_vaincus(a, nom):
    """ Arbre, str -> [str]
    Renvoie la liste des joueurs vaincus par nom dans la compétition d'arbre a """
    n = recherche_noeud(a, nom)
    return vaincus_gagnant(n)
