

def main():
    t = int(raw_input())
    for test_case in range(t):
        s = raw_input()
        mcount = 0
        pcount= 0
        n = len(s)
        for i in range(0,n):
            if s[i]!="+" and i%2==0:
                pcount+=1
            elif s[i]!="-" and i%2!=0:
                pcount+=1
        for i in range(0,n):
            if s[i]!="-" and i%2==0:
                mcount+=1
            elif s[i]!="+" and i%2!=0:
                mcount+=1
        print min(mcount,pcount)

if __name__=="__main__":
    main()
