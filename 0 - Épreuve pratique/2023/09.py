#Ex 1
def multiplication(n1,n2):
   res=0 
   for i in range(abs(n2)):
       res= res+n1
   return res

#Ex 2
def chercher(tab, n, i, j):
 if i < 0 or j > len(tab):
 return None
 elif i > j:
 return None
 m = (i + j) // ...
 if ... < n:
 return chercher(tab, n, ..., ...)
 elif ... > n:
 return chercher(tab, n, ..., ...)
 else:
 return ...
