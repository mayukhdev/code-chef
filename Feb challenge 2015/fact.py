fact = {}

def factorial(n):
    if n in fact:  
        return fact[n]
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        f = n *factorial(n-1)
        fact[n] = f
        return f


