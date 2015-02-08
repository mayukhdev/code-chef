def main():
    t = int(raw_input())
    for test_case in range(t):
        n = int(raw_input())
        pile = map(int,raw_input().split())
        #pile.sort()
        times = {}
        count=1
        for e in pile:
            if e not in times:
                times[e]=1
            else:
                times[e]+=1
        for key in times:
            if times[key]>count:
                count = times[key]
        print n-count
        

if __name__=="__main__":
    main()
