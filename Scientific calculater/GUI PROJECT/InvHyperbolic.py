from LogAlog import ln

def invsinh(x):     #Domain: (- ∞, ∞)
    a=((x**2)+1)**(1/2)
    b= x+(a)
    c=ln(b)
    return c

def invcosh(x):     #Domain: [1, ∞) 
    if x<0.9:
        return "Error"
    else:
        a=((x**2-1))**(1/2)
        b= x+a
        c= ln(b)
        return c

def invtanh(x):     #Domain: (-1, 1)
    if x<=-1 or x>=1:
        return "Error"
    else:
        a= 1+x
        b= 1-x
        c= a/b
        d= ln(c)
        return (1/2)*d

def invcoth(x):     #Domain (- ∞, -1) or (1, ∞)
    if x>=-1 and x<=1:
        return "Error"
    else:
        a= x+1
        b= x-1
        c= a/b
        d= ln(c)
        return (1/2)*d

def invsech(x):     #Domain (0, 1]
    if x<0 or x>1.1:
        return "Error"
    else:
        a= ((1/x**2)-1)**(1/2)
        b= 1/x
        c= a+b
        d= ln(c)
        return d

def invcosech(x):       #Domain: (- ∞, ∞)
    a= ((1/x**2)+1)**(1/2)
    b= 1/x
    c= a+b
    d= ln(c)
    return d
    
