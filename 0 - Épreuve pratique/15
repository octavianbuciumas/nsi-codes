#----------------------SUJET-15--------------------------#
#----------------------EXERCICE-1------------------------#
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def return_min(moy, a):
    tmin = t_moy[0]
    for t in range(len(moy)):
        if moy[t] < tmin:
            tmin = t_moy[t]
            amin = a[t]
        else:
            pass
    
    print(tmin,",",amin)

return_min(t_moy, annees)

#---------------------EXERCICE-2-------------------------#

def inverse_chaine(c):
    c_final = ""
    chaine = c
    for char in range(len(chaine)):
        c_final = c_final + chaine[-1] 
        chaine = chaine[:-1] 
    return c_final


print(inverse_chaine("Adam"))

def est_palindrome(c):
    if inverse_chaine(c) == c:
        return True
    else:
        return False
    
print(est_palindrome("121"))

def est_nbre_palindrome(n):
    if est_palindrome(str(n)):
        return True
    else:
        return False
    

print(est_nbre_palindrome(343))
