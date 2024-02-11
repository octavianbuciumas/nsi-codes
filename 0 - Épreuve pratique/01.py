def verifie(tab):
    """list --> bool"""
    n = len(tab)
    for i in range(n-1):
        if tab[i]>tab[i+1]:
            return False
    return True
    

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {'A' : 0,
                    'B' : 0,
                    'C' : 0}
    for bulletin in urne:
        if bulletin == 'A' or bulletin == 'B' or bulletin == 'C':
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            pass
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat]>nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
