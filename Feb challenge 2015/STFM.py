#passed only 1 subtask
import math

fact = {}

def approx(n,m):
    return int(math.factorial(n)%m)
##    first = math.sqrt(((2%m)*(math.pi%m)*(n%m))%m)
##    second = ((n%m) * math.e)
##    return first * second    

def factorial(n,m):
    if n>m:
        return 0
    elif m>100: #remove otherwise
        return approx(n,m)
    if n in fact:  
        return fact[n]
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        f = ((n%m) * (factorial(n-1,m)%m))%m
        fact[n] = f
        return f

def factorial_iter(n,m):
    fact[1]= 1%m
    fact[2]= 2%m
    if m>2:
        for i in range(3,m):
            fact[i] = ((i%m) * (fact[i-1]%m))%m
    if n<=m:
        return fact[n]
    else:
        return 0

def F(num,m):
    temp = 0
    for i in range(1,num+1):
        temp = (temp%m + ((i%m) * (factorial(i,m)%m+num%m))%m)%m
    return temp
        

def main():
    n,m = map(int,raw_input().split())
    p = map(int,raw_input().split())
    answer = 0
    for num in p:
        answer = (answer%m + F(num,m)%m)%m
    print answer
    
if __name__=="__main__":
    main()
