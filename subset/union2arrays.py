def isSubset( a1, a2, n, m):
    
    if set(a2)<=set(a1):
        remaining = set(a1)-set(a2)
        for x in remaining:
            while x in a1:
                a1.remove(x)
        a1.sort()
        a2.sort()
        if a2==a1:
            return("Yes")
        else:
            return("No")
    else:
          return("No")
