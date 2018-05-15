def sinh(x):
    b=(-1)*x
    a=((2.71828**x)-(2.71828**b))/2
    return (a)

def cosh(x):
    b=(-1)*x
    a=((2.71828**x)+(2.71828**b))/2
    return (a)    

def tanh(x):
    c=(-1)*x
    a=((2.71828**x)-(2.71828**c))/2
    b=((2.71828**x)+(2.71828**c))/2
    return(a/b)

def coth(x):
    c=(-1)*x
    a=((2.71828**x)-(2.71828**c))/2
    b=((2.71828**x)+(2.71828**c))/2
    return (b/a)

def cosech(x):
    b=(-1)*x
    a=((2.71828**x)-(2.71828**b))/2
    return (1/a)

def sech(x):
    b=(-1)*x
    a=((2.71828**x)+(2.71828**b))/2
    return (1/a) 
    
