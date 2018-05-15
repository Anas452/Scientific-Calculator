def fac(a):
    if a<0:
        return "Error"
    if a==0:
        return 1
    else:
        return (a*fac(a-1))
