class Chat:
    def bonjour(self):
        print("miaou")
        
class Chien:
    def bonjour(self):
        print("ouaf")
        
c = Chat()
b = c
c.bonjour()

c = Chien()
b.bonjour()







