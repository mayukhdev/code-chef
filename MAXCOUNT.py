def main():
    t = int(raw_input())
    nInt = []
    for times in range(t):
        n = int(raw_input()) #len of array
        inp = map(int,raw_input().split())
        value = 0
        count = 0
        for i in range(10001):
            nInt.append(0)
        for i in range(n):
            nInt[inp[i]]+=1
        for i in range(len(nInt)):
            if nInt[i]>count:
                count = nInt[i]
                value = i
        print str(value)+" "+str(count)
        inp = []
        nInt = []

if __name__=="__main__":
    main()
