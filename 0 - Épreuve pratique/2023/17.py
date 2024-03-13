def moyenne(liste_notes): #exercice 1
    """[(note, coef)]"""
    coef = 0
    notes = 0
    for i in range(len(liste_notes)):
        a, b = liste_notes[i]
        coef += b
        for i in range(b):
            notes += a  
    return notes/coef
        
def pascal(n): #exercice 2
    triangle= [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k-1][i-1] + triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle
