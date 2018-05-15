def QuadRoots(a,b,c):
    if a == 0:
        return "It does not form Quadratic equation."
    else:
        x1=((-(b)+((b**2)-(4*a*c))**.5)/(2*a))
        x2=((-(b)-((b**2)-(4*a*c))**.5)/(2*a))
        return(x1,x2)
        

