import math

output=[]
#output = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181, 18481, 19391, 19891, 19991, 30103, 30203, 30403, 30703, 30803, 31013, 31513, 32323, 32423, 33533, 34543, 34843, 35053, 35153, 35353, 35753, 36263, 36563, 37273, 37573, 38083, 38183, 38783, 39293, 70207, 70507, 70607, 71317, 71917, 72227, 72727, 73037, 73237, 73637, 74047, 74747, 75557, 76367, 76667, 77377, 77477, 77977, 78487, 78787, 78887, 79397, 79697, 79997, 90709, 91019, 93139, 93239, 93739, 94049, 94349, 94649, 94849, 94949, 95959, 96269, 96469, 96769, 97379, 97579, 97879, 98389, 98689, 1003001]


def isPali(m):
    temp = str(m)
    #L = int(math.ceil(len(temp)/2))
    #if temp[0:len(temp)/2] == temp[-1:-L-1:-1]:
    if temp[:] == temp[::-1]:
        return True
    return False
    
def isPrime(m):
    if m==2 or m==3:
        return True
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

def preprocess():
    pri = []
    n = range(1,1003002)
    for q in n:
        if isPrime(q):
            pri.append(q)
    for p in pri:
        if isPali(p):
            output.append(p)

def main():
    preprocess()
    #print "done"
    n = int(raw_input())
    i = 0
    while True:
        if n <= output[i]:
            print output[i]
            break
        else:
            i+=1
    

if __name__=="__main__":
    main()
