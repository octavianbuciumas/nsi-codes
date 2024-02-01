from ArbreBinaire import Noeud, ArbreBinaire, ABR

a_vide = ArbreBinaire()    
feuille1 = ArbreBinaire(Noeud(1,
                              ArbreBinaire(),
                              ArbreBinaire()))
feuille2 = ArbreBinaire(Noeud(2,
                              ArbreBinaire(),
                              ArbreBinaire()))
a0 = ArbreBinaire(Noeud(3, feuille1, feuille2))
a1 = ArbreBinaire()
tab = [1, 2, 3] 
a1.ajouter_depuis_tableau(tab)
a2 = ArbreBinaire()
a2.ajouter_depuis_tableau([3, 1, 4, None, 2, None, None])
a3 = ArbreBinaire()
a3.ajouter_depuis_tableau([3, 2, 4, 1])
a4 = ArbreBinaire()
a4.ajouter_depuis_tableau([3, 2, 4, None, 1])
a5 = ArbreBinaire()
a5.ajouter_depuis_tableau([3, 2, 6, 0, 4])
a6 = ArbreBinaire()
a6.ajouter_depuis_tableau([3, 1, 5, None, None, 2, 9])
a7 = ArbreBinaire()
for i in range(7):
    a7.inserer(i)
a8 = ArbreBinaire()
a8.ajouter_depuis_tableau([4, 3, 6, 2, 1, 7, 8])
a9 = ArbreBinaire()
a9.ajouter_depuis_tableau([4, 5, 6, 2, 8, 5, 7])
a10 = ArbreBinaire()
a10.ajouter_depuis_tableau([5, 4, 9, 2, 3, 7, 8])
a11 = ArbreBinaire()
a11.ajouter_depuis_tableau([8, 5, 10, 1, 6, 9, 12])

abr_vide = ABR()    
abr_feuille1 = ABR(Noeud(1,
                     ABR(),
                     ABR()))
abr_feuille2 = ABR(Noeud(3,
                     ABR(),
                     ABR()))
a11 = ABR(Noeud(2, abr_feuille1, abr_feuille2))
a12 = ABR()
a12.inserer(2)
a12.inserer(1)
a12.inserer(3)
a12.inserer(5)
