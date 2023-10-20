class Animal:
    pass

def creer_animal(e, n, c):
    ani = Animal()
    ani.espèce = e
    ani.nom = n
    ani.cri = c
    return ani

canard = creer_animal("cairina moschata",
    "Donald",
    "coin")

def crier(animal):
    print(f"Le {animal.espèce} {animal.nom} fait {animal.cri}")

crier(canard)

def indices_occurrences(tab, e):
    lst = []
    for i in range(len(tab) - 1, -1, -1):
        if tab[i] == e:
            lst.append(i)
    return lst

print(indices_occurrences(
    [1, 0, 0, 1, 0, 1],
    1))
