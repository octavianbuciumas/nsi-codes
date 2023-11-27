def repr_str(e):
    if isinstance(e, int): return str(e)
    if isinstance(e, str): return '"' + str(e) + '"'
def creer_pile_vide(): return []
def est_pile_vide(pile): return pile == []
def empiler(pile,element): pile.append(element)
def depiler(pile): return pile.pop()
def affiche_pile(p):
    if len(p) == 0:
        print("Pile vide")
        return
    s = ""
    c = max([len(repr_str(i)) for i in p])
    s += f"| {repr_str(p[-1]).center(c)} | -> sommet\n"
    for i in range(len(p)-2, -1, -1):
        s += f"| {repr_str(p[i]).center(c)} |\n"
    s += "-"* (c + 4)
    print(s)
        
def creer_file_vide(): return []
def est_file_vide(file): return file == []
def enfiler(pile,element): pile.append(element)
def defiler(pile): return pile.pop(0)

def affiche_file(f):
    if len(f) == 0:
        print("File vide")
        return
    c = " ".join(repr_str(e) for e in reversed(f))
    l = " "*len("enfilement -> ") + "-"*len(c) + " "*len(" -> défilement")
    c = "enfilement -> " + c + " -> défilement"
    print(f"{l}\n{c}\n{l}")
