#Using greedy approach with heaviest pie <= heaviest cooler.
def coolPie():
    nPie = int(raw_input())
    wPie = map(int,raw_input().split())
    wLimit = map(int,raw_input().split())
    wPie.sort(reverse=True)
    wLimit.sort(reverse=True)
    maxPie = 0
    j = 0 #counter for wLimit
    for i in range(len(wPie)):
        if wLimit[j] >= wPie[i]:
            maxPie+=1
            j+=1
        else:
            continue
    return maxPie
    
def main():
    t = int(raw_input())
    for i in range(t):
        print coolPie()

if __name__=="__main__":
    main()
