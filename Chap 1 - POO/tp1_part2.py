class Livre:
    def __init__(self, t, a, n):
        self.titre = t
        self.auteur = a
        self.nb_pages = n
        self.disponible = 1

    def affiche(self):
        """ Livre -> None """
        titre_livre = self.titre
        auteur_livre = self.auteur
        pages_tot = self.nb_pages
        print(f"< Livre '{titre_livre}', auteur {auteur_livre}, nombre de pages {pages_tot} >")

    def prix_base(self, prix_page):
        """ Livre -> float
        Calcule le prix de base d'un livre, à 12 centimes la page """
        return prix_page*self.nb_pages/100
        
    def prix_réduit(self, prix_page, reduc):
        """ Livre, int -> float
        Renvoie le prix du livre après réduction """
        # return (1 - reduc/100)*self.nb_pages*0.12
        return (1 - reduc/100)*self.prix_base(prix_page)

    def recevoir(self, n):
        self.disponible += n
        
    def vendre(self, prix_page, prix_reduc):
        if self.disponible < 1:
            return 0
        prix = self.prix_réduit(prix_page, prix_reduc)
        self.disponible -= 1
        return prix


def recherche(collection, titre):
    """ [Livre], str, -> int """
    for lvr in collection:
        if lvr.titre == titre:
            return lvr.disponible
    return 0
    
class Librairie:
    def __init__(self, c):
        """ Libraire, [Livre] -> NoneType"""
        self.collection = c
        
    def ajoute(self, lvr):
        """ Librairie, Livre -> NoneType """
        self.collection.append(lvr)
        
    def __str__(self):
        """ Librairie -> str """
        reponse = ""
        for lvr in self.collection:
            reponse += f"Livre {lvr.titre}, auteur {lvr.auteur},\
nombre de pages {lvr.nb_pages}\n"
        return reponse

livre1 = Livre("La peste", "Camus Albert", 59)
livre2 = Livre("Fondation", "Asimoov Isaac", 265)
livre4 = Livre("Les misérables", "Hugo Victor", 2135)
collection = [livre1, livre2, livre4]

lib_vide = Librairie([])
livre1 = Livre("La peste", "Camus", 59)
livre1.recevoir(7)
# ou
# livre.disponible = 8
livre2 = Livre("Fondation", "Asimov", 256)
livre2.recevoir(1)
livre3 = Livre("Les misérables", "Hugo", 2135)
livre3.recevoir(14)
livre4 = Livre("Harry Potter", "Rowling", 132)
livre4.recevoir(4)


lib = Librairie([livre1, livre2, livre3, livre4])

livre5 = Livre("Le roi Babar", "Jean de Brunhoff", 15)
livre5.recevoir(10)
lib.ajoute(livre5)






































