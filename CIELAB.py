def main():
    inp = map(int,raw_input().split())
    ans = inp[0] - inp[1]
    if ans%10==9:
        ans-=1
    else:
        ans+=1
    print ans

if __name__=="__main__":
    main()
