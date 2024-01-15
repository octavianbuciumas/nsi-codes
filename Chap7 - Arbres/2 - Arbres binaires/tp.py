from ds import Arbre, creer_vide, est_vide, gauche, droit, etiquette

a0 = Arbre(5, None, None)
a1 = Arbre(-2, None, None)
a2 = Arbre(1, a0, a1)
a3 = Arbre(1,
           Arbre(4,
                 None,
                 Arbre(3, None, None)),
           Arbre(5,
                 Arbre(2,
                       Arbre(12, None, None),
                       Arbre(9, None, None)),
                 Arbre(1,
                       Arbre(7, None, None),
                       None)))

a4 = Arbre(9, Arbre(7, None, None), None)
a5 = Arbre(8, Arbre(5, None, None), None)
a6 = Arbre(1, Arbre(2, None, None), Arbre(3, None, None))
a7 = Arbre(12,
           a6,
           Arbre(4,
                 Arbre(9,
                       Arbre(7, None, None),
                       None),
                 Arbre(8, None, Arbre(5, None, None))))

def est_feuille(a):
    """ Arbre -> bool
    Détermine si a est constitué d'un seul élément """
    # lorsque l'arbre est vide not est_vide(a) s'évalue à False
    # python n'évalue pas le reste car False and ... vaudra toujours False
    # Donc les instructions gauche(a) et droit(a) ne sont pas exécutées
    # lorsque l'arbre a est vide.
    return not est_vide(a) and est_vide(gauche(a)) and est_vide(droit(a)) 
    
    # if gauche(a) == None and droit(a) == None and creer_vide() != a:
    #    return True
    # return False

def taille(a):
    """ Arbre -> int
    Renvoie le nombre de nœuds de a """
    if est_vide(a):
        return 0
    else:
        # 2 appels récursifs
        return 1 + taille(gauche(a)) + taille(droit(a))
        

def somme(a):
    """ Arbre -> int
    Renvoie la somme des éléments de l'arbre a """
    # cas de base avec un élément plus compliqué :
    if est_feuille(a):
        return etiquette(a)
    elif est_vide(droit(a)):
        return somme(gauche(a)) + etiquette(a)
    elif est_vide(gauche(a)):
        return somme(droit(a)) + etiquette(a)
#    if taille(a) == 1:
#        return etiquette(a)
#    if est_vide(a):
#        return 0
    else:
        return somme(gauche(a)) + somme(droit(a)) + etiquette(a)
    
def produit(a):
    """ Renvoie le produit des éléments de a """
    # le produit de zéro éléments vaut 1
    # (mais pourquoi ???? parce que ça marche !)
    if est_vide(a):
        return 1
    else:
        return produit(gauche(a))*produit(droit(a))*etiquette(a)

def hauteur(a):
    """ Arbre -> int
    Renvoie la hauteur de l'arbre """
#    if est_vide(a):
# return 0
    if est_feuille(a):
        return 1
    elif est_vide(droit(a)):
        return hauteur(gauche(a)) + 1
    elif est_vide(gauche(a)):
        return hauteur(droit(a)) + 1
    else:
        max_gauche = hauteur(gauche(a))
        max_droite = hauteur(droit(a))
        if max_gauche > max_droite :
            return max_gauche + 1
        else:
            return max_droite + 1
        

def affiche_infixe(a):
    """ Arbre -> Nonetype
    Affiche l'arbre a de manière infixe """
    if est_vide(a):
        pass
    else:
        print("(", end="")
        affiche_infixe(gauche(a))
        print(etiquette(a), end="")
        affiche_infixe(droit(a))
        print(")", end="")

def affiche_prefixe(a):
    """ Arbre -> Nonetype
    Affiche l'arbre a de manière infixe """
    if est_vide(a):
        pass
    else:
        print("(", end="")
        print(etiquette(a), end="")
        affiche_prefixe(gauche(a))
        affiche_prefixe(droit(a))
        print(")", end="")

def affiche_postfixe(a):
    """ Arbre -> Nonetype
    Affiche l'arbre a de manière infixe """
    if est_vide(a):
        pass
    else:
        print("(", end="")
        affiche_postfixe(gauche(a))
        affiche_postfixe(droit(a))
        print(etiquette(a), end="")
        print(")", end="")

def rechercher(a, e):
    """ Arbre, int -> bool
    Renvoie True ssi e est une des étiquettes de a """
    if est_vide(a):
        return False
#    ou mieux :
#    elif etiquette(a) == e:
#        return True
    else:
        avant_gauche = rechercher(gauche(a), e)
        avant_droit =  rechercher(droit(a), e)
        # un élément e est une étiquette de l'arbre de racine a
        # si
        # soit il appartient au sous-arbre gauche
        # soit il appartient au ssous-arbre droit
        # soit c'est l'étiquette de la racine
        return avant_gauche or avant_droit or etiquette(a) == e
        

def maximum(a):
    """ Arbre -> int
    Renvoie la plus grande étiquette de a """
    if est_feuille(a):
        return etiquette(a)
    elif est_vide(gauche(a)):
        avant_droit = maximum(droit(a))
        if avant_droit > etiquette(a):
            return avant_droit
        else:
            return etiquette(a)
    elif est_vide(droit(a)):
        # attention à ne pas confondre max et maximum
        return max(etiquette(a), maximum(gauche(a)))
        #avant_gauche = maximum(gauche(a))
        #return avant_gauche if avant_droit > etiquette(a) else etiquette(a)
    else:
        return max(etiquette(a), maximum(gauche(a)), maximum(droit(a)))

def est_egal(a1, a2):
    """ Arbre, Arbre -> bool
    Détermine si les arbres a1 et a2 sont identiques """
    pass

def est_egalf(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True si et seulement si les arbres a1 et a2 sont faiblement égaux """
    pass

def contenu(a, d):
    """ Arbre, dict -> Nonetype
    Ajoute à d le contenu de a """
    pass

def est_dico_egal(d1, d2):
    """ dict, dict -> bool
    Détermine si les dictionnaires d1 et d2 sont égaux """
    pass

def est_egalc(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True ssi les arbres a1 et a2 ont le même contenu """
    pass

