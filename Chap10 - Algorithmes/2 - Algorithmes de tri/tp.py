from ds import *

def tab_est_trie(tab):
    """ [int] -> bool
    Détermine si le tableau tab est trié par ordre croissant. """
    for i in range(len(tab) - 1):
        if tab[i] > tab[i+1]:
            return False
    return True

def liste_est_triee(l):
    """ Liste -> bool
    Détermine si la liste l est triée """
    if est_vide(l) or est_singleton(l):
        return True
    else:
        reste = liste_est_triee(queue(l))
        x1, x2 = tete(l), tete(queue(l))
        return x1 <= x2 and reste 
        

def tri_insertion_iter(tab):
    """ [int] -> [int]
    Trie en place le tableau tab (tri par insertion) """
    n = len(tab)
    for i in range(n):
        # les éléments d'indice 0..i du tableau t
        # sont triés dans l'ordre croissant
        element = tab[i]
        trou = i
        # on cherche à insérer l'élément dans le tableau
        # constitué des éléments d'indice 0..i
        while tab[trou - 1] > element and trou > 0:
            tab[trou] = tab[trou-1]         # on décale l'élément précédent de tab
            trou = trou - 1              # mise à jour de l'indice du trou
        # À la fin de la boucle soit
        # trou = 0 et tous les éléments de t sont supérieurs à élément
        # soit trou > 0, t[trou - 1] < element < t[i] pour tout i >= trou
        tab[trou] = element
        # le tableau est alors trié
    return tab # que se passe-t-il si on ne le met pas ?

def insere_trie(l, e):
    """ Liste, int -> Liste
    l est triée par ordre croissant """
    if est_vide(l):
        return ajoute(l, e)
    else:
        if e < tete(l):
            return ajoute(l, e)
        else:
            a = insere_trie(queue(l),e)
            return ajoute(a, tete(l))

def trie_insertion_rec(l):
    """ Liste -> Liste
    Trie la liste l à l'aide de l'algorithme du tri par insertion """
    if est_vide(l):
        return l
    else:
        reste = trie_insertion_rec(queue(l))
        return insere_trie(reste, tete(l))

def mini_a_partir(tab, i):
    """ [int], int -> int
    Renvoie l'indice du plus petit élément de tab à partir de l'indice i """
    pass

def tri_selection_iter(tab):
    """ [int] -> [int]
    Trie le tableau tab (tri par sélection) """
    pass

def minimum(l):
    """ Liste -> int
    l est non vide
    Renvoie le plus petit élément de la liste l """
    pass

def supprime(l, e):
    """ Liste, int -> Liste
    l est non vide, e appartient à l
    Renvoie la liste l où on a supprimé une occurence de e """
    pass

def tri_selection_rec(l):
    """ Liste -> Liste
    Trie la liste l (tri par sélection) """
    pass

def diviser(l):
    """ Liste -> Liste, Liste
    Divise la liste en deux listes """
    if est_vide(l):
        return creer_vide(), creer_vide()
    elif est_singleton(l):
        return l, creer_vide()
    else:
        l1, l2 = diviser(queue(queue(l)))
        l1 = ajoute(l1, tete(l))
        l2 = ajoute(l2, tete(queue(l)))
        return l1, l2

def fusionner(l1, l2):
    """ Liste, Liste -> Liste
    Renvoie la liste des éléments de l1 et l2 triés """
    if est_vide(l1) and est_vide(l2):
        return creer_vide()
    elif est_vide(l1):
        return l2
    elif est_vide(l2):
        return l1
    else:
        # ALGORITHME INCORRECT :
        # fusionner((1, 3), (5, 6)) renvoie
        # (1, 5, 3, 6)
        # qui n'est pas triée par ordre croissant
        # En effet, si on met 1 et 5 "à part" et que
        # l'on fusionne récursivement les queues,
        # on obtient la liste (3, 6). Or 5 est plus
        # grand que 3 ! Ça ne marche donc pas dans ce cas.
#        x1, x2 = tete(l1), tete(l2)
#        reste = fusionner(queue(l1), queue(l2))
#        if x2 > x1:
#            reste = ajoute(reste, x2)
#            reste = ajoute(reste, x1)
#        else:
#            reste = ajoute(reste, x1)
#            reste = ajoute(reste, x2)
        # ALGORITHME CORRECT :
        # x1 et x2 sont les deux premiers éléments
        # des listes l1 et l2, triées par ordre croissant
        x1, x2 = tete(l1), tete(l2)
        # si x1 < x2, alors on est certain qu'il
        # sera le premier élément de la liste fusionnée.
        # On fusionne donc queue(l1) avec l2
        # (c'est possible, car il y a au total un élément
        # de moins dans ces deux listes, l'élément x1)
        # Puis, il suffit d'ajouter x1 en début de liste.
        if x1 < x2:
            reste = fusionner(queue(l1), l2)
            reste = ajoute(reste, x1)
        # idem "dans l'autre sens"
        # si x2 est le plus petit élément.
        else:
            reste = fusionner(l1, queue(l2))
            reste = ajoute(reste, x2)            
        return reste
            
    
def fusionner_2(l1, l2):
    """ Liste, Liste -> Liste
    l1 et l2 sont triées
    Renvoie la liste des éléments de l1 et l2 triés """
    liste_triee = creer_vide()
    while not est_vide(l1) and not est_vide(l2):
        if tete(l1) > tete(l2):
            liste_triee = ajoute(liste_triee,tete(l2))
            l2 = queue(l2)
        else:
            liste_triee = ajoute(liste_triee,tete(l1))
            l1 = queue(l1)
    while not est_vide(l1):
            liste_triee = ajoute(liste_triee,tete(l1))
            l1 = queue(l1)
    while not est_vide(l2):
            liste_triee = ajoute(liste_triee,tete(l2))
            l2 = queue(l2)
    rep = creer_vide()
    while not est_vide(liste_triee):
        rep = ajoute(rep, tete(liste_triee))
        liste_triee = queue(liste_triee)
    return rep
    

def tri_fusion(l):
    """ Liste -> Liste
    Trie la liste l (tri fusion) """
    if est_vide(l) or est_singleton(l):
        return l
    else:
        l1, l2 = diviser(l)
        l1 = tri_fusion(l1)
        l2 = tri_fusion(l2)
        return fusionner(l1, l2)
        
# visualisation en ligne : https://www.recursionvisualizer.com/?function_definition=def%20diviser%28tab%29%3A%0A%20%20%20%20%22%22%22%20Liste%20-%3E%20Liste%2C%20Liste%0A%20%20%20%20Divise%20la%20liste%20en%20deux%20listes%20%22%22%22%0A%20%20%20%20if%20len%28tab%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%5B%5D%2C%20%5B%5D%0A%20%20%20%20elif%20len%28tab%29%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20tab%2C%20%5B%5D%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20l1%2C%20l2%20%3D%20diviser%28tab%5B2%3A%5D%29%0A%20%20%20%20%20%20%20%20x%2C%20y%20%3D%20tab%5B0%3A2%5D%20%0A%20%20%20%20%20%20%20%20return%20%5Bx%5D%20%2B%20l1%2C%20%5By%5D%20%2B%20l2%0A%0Adef%20fusionner%28l1%2C%20l2%29%3A%0A%20%20%20%20%22%22%22%20Liste%2C%20Liste%20-%3E%20Liste%0A%20%20%20%20Renvoie%20la%20liste%20des%20%C3%A9l%C3%A9ments%20de%20l1%20et%20l2%20tri%C3%A9s%20%22%22%22%0A%20%20%20%20if%20len%28l1%29%20%3D%3D%200%20and%20len%28l2%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20%5B%5D%0A%20%20%20%20elif%20len%28l1%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20l2%0A%20%20%20%20elif%20len%28l2%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20l1%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20x1%2C%20x2%20%3D%20l1%5B0%5D%2C%20l2%5B0%5D%0A%20%20%20%20%20%20%20%20if%20x1%20%3C%20x2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20reste%20%3D%20fusionner%28l1%5B1%3A%5D%2C%20l2%29%0A%20%20%20%20%20%20%20%20%20%20%20%20reste%20%3D%20%5Bx1%5D%20%2B%20reste%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20reste%20%3D%20fusionner%28l1%2C%20l2%5B1%3A%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20reste%20%3D%20%5Bx2%5D%20%2B%20reste%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20reste%0A%0Adef%20tri_fusion%28l%29%3A%0A%20%20%20%20%22%22%22%20Liste%20-%3E%20Liste%0A%20%20%20%20Trie%20la%20liste%20l%20%28tri%20fusion%29%20%22%22%22%0A%20%20%20%20if%20len%28l%29%20%3C%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20l%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20l1%2C%20l2%20%3D%20diviser%28l%29%0A%20%20%20%20%20%20%20%20l1%20%3D%20tri_fusion%28l1%29%0A%20%20%20%20%20%20%20%20l2%20%3D%20tri_fusion%28l2%29%0A%20%20%20%20%20%20%20%20return%20fusionner%28l1%2C%20l2%29%0A&function_call=tri_fusion%28%5B3%2C%206%2C%201%2C%205%5D%29
        
        
        
        
        
        
        
        
        
        

