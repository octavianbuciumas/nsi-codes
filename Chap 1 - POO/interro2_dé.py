from random import randint

class Dé:
    def __init__(self, nb_faces):
        self.nb_faces = nb_faces
        self.dernier_lancer = 0
        
    def lancer(self):
        N = randint(1, self.nb_faces)
        self.dernier_lancer = N
        return N
    
    def __str__(self):
        return f"Le résultat du dé est {self.dernier_lancer}"
    
    
d = Dé(20)
d.lancer()
print(d)