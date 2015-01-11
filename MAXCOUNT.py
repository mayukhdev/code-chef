def main():
    t = int(raw_input())
    for times in range(t):
        inp = []
        nInt = {}
        n = int(raw_input()) #len of array
        inp = map(int,raw_input().split())
        value = 0
        count = 0
        for i in range(n):
            nInt[inp[i]]=0
        for i in range(n):
            nInt[inp[i]]+=1
        for val in nInt:
            if nInt[val]>=count:
                if count==0:
                    value = val
                elif value>val and nInt[val]==count and count!=0:
                    value = val
                elif nInt[val]>count:
                    value = val
                count = nInt[val]

        print str(value)+" "+str(count)
        

if __name__=="__main__":
    main()
