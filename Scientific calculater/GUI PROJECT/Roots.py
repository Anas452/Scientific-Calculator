def sqrt(x):
    if x<0:
        return "Math Error"
    else:
        return ((x)**(1/2))
def cbrt(x):
    if x<0:
        x=-(x)
        return -((x)**(1/3))
    else:
        return ((x)**(1/3))

def nthrt(x,n):
    if n%2==0:
        if x<0:
            return "Math Error"
        else:
            return ((x)**(1/n))
    if n%2==1:
        if x<0:
            x=-(x)
            return -((x)**(1/n))
        else:
            return ((x)**(1/n))

