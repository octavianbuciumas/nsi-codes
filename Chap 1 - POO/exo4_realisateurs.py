class Personne:
    def __init__(self, nom, année_naissance, lieu_naissance):
        """ str, int, str -> None """
        self.nom = nom
        self.année_naissance = année_naissance
        self.lieu_naissance = lieu_naissance

    def __str__(self):
        # print(real) est la même chose que
        # print(real.__str__())
        # Cette méthode spéciale
        # permet d'expliquer comment
        # l'objet doit être affiché
        # lorsqu'il est appelé avec
        # l'instruction print. 
        return f"{self.nom} est né en {self.année_naissance} à {self.lieu_naissance}."

class Film:
    def __init__(self, titre, réalisateur):
        """ Film, str, Personne -> None """
        self.titre = titre
        self.réalisateur = réalisateur

    def __str__(self):
        return f"{self.titre} a été \
réalisé par {self.réalisateur.nom}\
originaire de \
{self.réalisateur.lieu_naissance}"

real = Personne("David Lynch",
                1946,
                "Missoula")

flm = Film("Dune",
           real)


# print(flm.titre)
# affiche "Dune"
# print(flm.réalisateur.nom)
# affiche "David Lynch"
# print(flm.réalisateur)
# affiche
# David Lynch est né en 1946
# à Missoula.
# Équivalent à
# print(flm.réalisateur.__str__())
# Attention à
# print(flm.réalisateur.__str__)









