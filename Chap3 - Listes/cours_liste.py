class Maillon:
    def __init__(self, v, n):
        self.suivant = n
        self.valeur = v

# culture générale
def creer_vide() -> Maillon: return None

def ajoute(m: Maillon, e: int) -> Maillon: return Maillon(e, m)
