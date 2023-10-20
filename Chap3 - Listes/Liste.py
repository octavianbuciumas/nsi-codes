class Liste:
    pass

def creer_vide() -> Liste: return ()
def est_vide(l: Liste) -> bool: return l == ()
def ajoute(l: Liste, e: int) -> Liste: return (e, l)
def tete(l: Liste) -> int: return l[0]
def queue(l: Liste) -> Liste: return l[1]
def affiche(l: Liste) -> None: print("x") if est_vide(l) else (print(tete(l), end = " - "), affiche(queue(l)))
def element(l: Liste, i: int) -> int: return tete(l) if i == 0 else element(queue(l), i - 1)