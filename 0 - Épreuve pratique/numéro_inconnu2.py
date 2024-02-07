# Auteur : Biranté

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def fusion( tab1 , tab2):
    """list,list -> list """
    table = []
    while tab1 != [] and tab2 != [] :
        if tab1[0] > tab2[0]:
            table.append(tab2.pop(0))
            table.append(tab1.pop(0))
    # Sans la méthode extend ?
    if tab1 == [] and tab2 != tab1 :
        table.extend(tab2)
    if tab2 == [] and tab1 != tab1 :
        table.extend(tab2)
    return table


def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """

    if len(nombre) == 1:
        return romains[nombre]

    elif romains[nombre[0]] >= 3:
        return romains[nombre[0]] + romains[nombre[1]]
    else:
        return
