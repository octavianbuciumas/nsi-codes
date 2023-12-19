from ds import *

class Processus:
    """Représente un processus"""
    def __init__(self, pid, arrivee, duree):
        """Processus, int, int, int -> Nonetype"""
        self.pid = pid
        self.arrivee = arrivee
        self.duree = duree
        self.duree_restante = duree
        self.debut = -1
        self.fin = -1
        
    def __repr__(self):
        """ Processus -> str
        Renvoie une chaine de caractère représentant le processus self """
        return f"<P{self.pid}>"
    
    def avancer(self, d, t):
        """ Processus, int, int -> Nonetype
        Le processus (re)prend son exécution à la date t pour une durée d """
        assert self.arrivee <= t
        # on enregistre la date du premier appel
        if self.debut == -1:
            self.debut = t
        # on avance le processus
        self.duree_restante -= d
        # on enregistre l'instant de fin 
        if self.est_termine():
            self.fin = t + d 
    
    def est_termine(self):
        """ Processus -> bool
        Détermine si le processus p a terminé son exécution """
        return self.duree_restante <= 0
        # if self.duree_restante <= 0:
        #     return True
        # return False
    
    def sejour(self):
        """ Renvoie le temps de séjour de self """
        return self.fin - self.arrivee
    
    def execution(self):
        """ Renvoie le temps d'exécution de self """
        return self.duree - self.duree_restante
    
    def attente(self):
        """ Renvoie le temps d'attente de self """
        return self.sejour() - self.execution()
    
    def latence(self):
        """ Renvoie le temps de latence de self """
        return self.debut - self.arrivee

class Chronogramme:
    """Représente un chronogramme"""
    def __init__(self):
        """Chronogramme -> Nonetype"""
        self.table = []

    def temps_ecoule(self):
        """ Chronogramme -> int
        Renvoie le nombre de cycles écoulés depuis l'instant initial """
        return len(self.table)
    
    def enregistrer(self, p, q):
        """ Chronogramme, int, int -> Nonetype
        Enregistre l'information : le processus p est exécuté pendant q cycles """
        for _ in range(q):
            self.table.append(p)
    
    def __repr__(self):
        """ Chronogramme -> str
        Renvoie une chaine de caractère représentant le chronogramme self """
        # return "|".join([str(p) for p in self.table])
        s = "|"
        for p in self.table:
           s += str(p) + "|"
        return s

class OrdonnanceurFIFO:
    """Représente un ordonnanceur"""
    def __init__(self, q=1):
        """OrdonnanceurFIFO, int -> Nonetype"""
        self.chrono = Chronogramme()
        self.file_processus = File()
        self.quantum = q

    def ajoute_processus(self, p_list):
        """ OrdonnanceurFIFO, [Processus] -> Nonetype
        Ajoute à self.file_processus les processus de p_list par ordre d'arrivée """
        while len(p_list) != 0:
            self.file_processus.enfiler(renvoie_et_supprime_premier(p_list))
        
    def exec_quantum(self):
        """ OrdonnanceurFIFO -> Nonetype
        Simule l'exécution d'un quantum """
        p = self.file_processus.examine()
        p.avancer(self.quantum, self.chrono.temps_ecoule())
        self.chrono.enregistrer(p, self.quantum)
        if p.est_termine():
            self.file_processus.defiler()
    
    def exec(self):
        """ OrdonnanceurFIFO -> Chronogramme
        Simule l'exécution des processus de la file et en renvoie le chronogramme """
        while not self.file_processus.est_vide():
            self.exec_quantum()
        return self.chrono

def renvoie_et_supprime_premier(p_list):
    """ [Processus] -> Processus
    Renvoie et supprime de p_list le processus dont l'attribut arrivee est le plus petit """
    mini = p_list[0].arrivee
    indice = 0
    for i in range(len(p_list)):
        if p_list[i].arrivee < mini :
            mini = p_list[i].arrivee
            indice = i
    # one-liner : (complètement hors programme)
    # indice, mini = min(enumerate(l), key=lambda t: t[1].arrivee)
    # explications : l'argument optinnel key est une fonction f
    # l'instruction 
    # min([P1, P2, P3], key=f) 
    # permet de renvoyer 
    # l'élément e du tableau [e1, e2, e3] tel que f(e) est mininum
    # enumerate([P1, P2, P3]) renvoie le tableau [(0, P1), (1, P2), (2, P3)]
    return p_list.pop(indice)

p1 = Processus(1, 0, 10)
p2 = Processus(2, 3, 4)
p3 = Processus(3, 2, 8)
l = [p1,p2,p3]
ordo = OrdonnanceurFIFO()
ordo.ajoute_processus(l)
#for _  in range(3):
#    ordo.exec_quantum()
