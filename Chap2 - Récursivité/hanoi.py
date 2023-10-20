from copain import mathieu, autre

PILIERS = ['A', 'B', 'C']

def zac(depart, arrivee):
    c = autre(depart, arrivee)
    mathieu(depart, c)
    print(f'{depart} --> {arrivee}')
    mathieu(c, arrivee)

def hanoi(n, depart, arrivee):
    """ int, str, str -> NoneType
    Affiche la liste des coups solutions pour
    le problème de hanoi, difficulté n. """
    if n == 1:
        print(f'{depart} --> {arrivee}')
    else:
        c = autre(depart, arrivee)
        # affiche la liste coup pour la difficulté inférieure
        # déplace n - 1 disques de départ au pilier intermédiaire
        hanoi(n - 1, depart, c)
        print(f'{depart} --> {arrivee}')
        # affiche la liste coup pour la difficulté inférieure
        # déplace n - 1 disques du pilier intermédiaire à l'arrivée
        hanoi(n - 1, c, arrivee) 