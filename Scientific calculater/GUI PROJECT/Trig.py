pi=3.14159265359

def sin(x):     #Domain (- ∞, ∞ )
    x=x*(pi/180)
    y=((x)-((1/6)*(x**3))+((1/120)*(x**5))-((1/5040)*(x**7))+((1/362880)*(x**9))-
            ((1/39916800)*(x**11))+((1/6227020800)*(x**13))-((1/1307674368000)*(x**15)))
    return round(y,5)

def cos(x):     #Domain (- ∞, ∞ )
    x=x*(pi/180)
    y=((1)-((1/2)*(x**2))+((1/24)*(x**4))-((1/720)*(x**6))+((1/40320)*(x**8))-
           ((1/3628800)*(x**10))+((1/479001600)*(x**12))-((1/87178291200)*(x**14)))
    return round(y,5)

def tan(x):         #Domain: All real numbers except  n*(pi/2)
    if x==90 or x==270:
        return "Error"
    else:
        return sin(x)/cos(x)

def cot(x):     #Domain: All real numbers except n*Pi
    if x==0 or x==90:
        return "Error"
    else:
        return 1/tan(x)

def sec(x):     #Domain: All real numbers except  n*(pi/2)
    if x==90:
        return "Error"
    else:
        return 1/cos(x)

def cosec(x):       #Domain: All real numbers except n*Pi
    if x==0:
        return "Error"
    else:
        return 1/sin(x)

