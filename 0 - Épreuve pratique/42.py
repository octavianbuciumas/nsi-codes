def tri_selection(tab):

    for i in range(len(tab)):
        min = i

        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
               min = j
        stock = tab[i]
        tab[i] = tab[min]
        tab[min] = stock

    return tab

#ex2---------------------------------------------------------

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10: 
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)
