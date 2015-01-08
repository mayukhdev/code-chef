import math

def isPali(m):
    temp = str(m)
    #L = int(math.ceil(len(temp)/2))
    #if temp[0:len(temp)/2] == temp[-1:-L-1:-1]:
    if temp[:] == temp[::-1]:
        return True
    return False
    
def isPrime(m):
    if m%2==0:
        return False
    sqr = int(math.sqrt(m))
    if m%sqr==0:
        return False
    elif sqr>2 and sqr%2==0:
        sqr-=1       
    for i in range(sqr,2,-2):
        if m%i==0:
            return False
    return True

def main():
    n = int(raw_input())
    m = n
    while True:
        if isPrime(m) and isPali(m):
            print m
            break
        else:
            if m%2==0:
                m+=1
            else:
                m+=2

if __name__=="__main__":
    main()
