def ceil(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

def floor(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1
