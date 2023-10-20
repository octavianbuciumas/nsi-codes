class Livre:
    def __init__(self, t, a, n):
        self.titre = t
        self.auteur = a
        self.nb_pages = n

# Livre("Les misérables", "Hugo Victor", 2135)
# créé un nouvel objet de type livre
# tout pareil que :
livre1 = Livre("Lesmisérables",
               "hugo",
               2135)
livre2 = Livre("Iron man",
               "marvel",
               45)
# la fonction __init__
# ajoutée à la classe
# permet de définir une fonction Livre
# qui prend trois arguments, et
# qui initialise un objet de type
# Livre de la bonne manière.

def affiche(lvr):
    """ Livre -> None
    Affiche le livre lvr """
    titre_livre = lvr.titre
    pages_tot = lvr.nb_pages
    auteur = lvr.auteur
    print(f"< Livre '{titre_livre}', auteur est {auteur}, nombre de pages {pages_tot} >")

def prix_base(lvr, prix_page):
    """ Livre, float -> float
    Calcule le prix de base d'un livre, à prix_page centimes la page """
    return prix_page * lvr.nb_pages/100
    
def prix_réduit(lvr, prix_page, reduc):
    """ Livre, float, int -> float
    Renvoie le prix du livre après réduction """
    prix_livre = prix_base(lvr, prix_page)
    return prix_livre*(1 - reduc/100)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    