class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplace(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def symetrique(self):
        return Point(-self.x, -self.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

a = Point(2, 4)
print(a)
b = Point(1, 2) # représente B(1 ; 2)
print(b)
b.deplace(3, 5)
print(b)
b.symetrique()
print(b)

class Segment:
    def __init__(self, d, f):
        self.debut = d
        self.fin = f
        
    def deplacer(self, dx, dy):
        """ Segment, float, float -> NoneType"""
        self.debut.deplace(dx, dy)
        self.fin.deplace(dx, dy)
        
    def symetrique(self):
        """ Segment -> Segment"""
        return Segment(
            self.debut.symetrique(),
            self.fin.symetrique()
            )
        # A le mérite de marcher...
        # return Segment(Point(-self.debut.x, -self.debut.y),
        #               Point(-self.fin.x, -self.fin.y))
        

s1 = Segment(a, b)
print(s1.debut, s1.fin)
s1.deplacer(2, 1)
print(s1.debut, s1.fin)
print(b) # b a été modifié par la méthode deplacer
s2 = s1.symetrique()
print(s2.debut, s2.fin)
print(b) # b n'a pas été modifié par la méthode symétrique
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
