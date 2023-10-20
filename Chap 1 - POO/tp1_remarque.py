class Livre:
    pass

livre1 = Livre()
livre1.titre = "La peste"
livre1.auteur = "Camus Albert"
livre1.nb_pages = 59

livre2 = Livre()
livre2.titre = "Fondation"
livre2.auteur = "Asimov"
livre2.nb_pages = 256

def créer_livre(t, a, n):
    # l est une variable locale
    l = Livre()
    l.titre = t
    l.auteur = a
    l.nb_pages = n
    return l

# on affecte à la variable globale
# livre3 le résultat revoyé par
# créer_livre
livre3 = créer_livre("Maik", "Bob", 123)