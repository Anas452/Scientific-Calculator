

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def log10(x):
    if x==0:
        return "Math Error"
    else:
        a=ln(10)
        return (ln(x))/a

def lognth(x,base):
    a=ln(base)
    return (ln(x))/a

def antilog(x):
    return 10**x
