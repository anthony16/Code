def recurExp(a,b):
    if b == 1:
        return a 
    else:
        return a * recurExp(a, b-1)