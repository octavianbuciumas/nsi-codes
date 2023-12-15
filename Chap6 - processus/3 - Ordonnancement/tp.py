from ds import *

class Processus:
    """Représente un processus"""
    def __init__(self, pid, arrivee, duree):
        """Processus, int, int, int -> Nonetype"""
        self.pid = pid
        self.arrivee = arrivee
        self.duree = duree
        self.duree_restante = duree
        
    def __repr__(self):
        """ Processus -> str
        Renvoie une chaine de caractère représentant le processus self """
        return f"<P{self.pid}>"
    
    def avancer(self, d, t):
        """ Processus, int, int -> Nonetype
        Le processus (re)prend son exécution à la date t pour une durée d """
        pass
    
    def est_termine(self):
        """ Processus -> bool
        Détermine si le processus p a terminé son exécution """
        pass    
    
    def sejour(self):
        """ Renvoie le temps de séjour de self """
        pass
    
    def execution(self):
        """ Renvoie le temps d'exécution de self """
        pass
    
    def attente(self):
        """ Renvoie le temps d'attente de self """
        pass
    
    def latence(self):
        """ Renvoie le temps de latence de self """
        pass

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
        """ int, int -> Nonetype
        Enregistre l'information : le processus p est exécuté pendant q cycles """
        pass
    
    def __repr__(self):
        """ self -> str
        Renvoie une chaine de caractère représentant le chronogramme self """
        pass

class OrdonnanceurFIFO:
    """Représente un ordonnanceur"""
    def __init__(self, q=1):
        """OrdonnanceurFIFO, int -> Nonetype"""
        pass

    def ajoute_processus(self, p_list):
        """ OrdonnanceurFIFO, [Processus] -> Nonetype
        Ajoute à self.file_processus les processus de p_list par ordre d'arrivée """
        pass
    
    def exec_quantum(self):
        """ OrdonnanceurFIFO -> Nonetype
        Simule l'exécution d'un quantum """
        pass
    
    def exec(self):
        """ OrdonnanceurFIFO -> Chronogramme
        Simule l'exécution des processus de la file et en renvoie le chronogramme """
        pass

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
        

