def kali(a,b):
    return a * b

def max3(x,y,z):
    if x >= y and x >= z:
        return x
    return max3(y,z,x)
    
