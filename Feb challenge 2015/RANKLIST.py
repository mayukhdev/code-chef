def main():
    t = int(raw_input())
    for test_case in range(t):
        n,s=map(int,raw_input().split())
        total = sum(range(1,n+1))
        diff = total - s
        #print "diff:",
        #print diff
        i=1
        lower=1
        upper= n-i
        num=1
        if diff==0: #sum(n)==s
            print 0
        else:
            while True:
                if diff>=lower and diff<=upper:
                    print num
                    break
                else:
                    i+=1
                    lower=upper+1
                    upper+=(n-i)
                    num+=1
##        total = 0
##        arr = []
##        num = 1                   
##        while total!=s or len(arr)!=n:
####            print arr,
####            print " num:",
####            print num
##            try:
##                if total==s:
##                    if len(arr)!=n and num>0:
##                        num-=1
##                        total-=num
##                        arr.pop()
##                        num-=1
##                elif num<=0:            
##                        last = arr.pop()
##                        total-=last
##                        num = last-1
##                elif total+num<=s:
##                    arr.append(num)
##                    total+=num
##                    num+=1
##                else:
##                    num-=1
##            except:
##                print "error in sum"
##                break
##        arr.sort()
##        print "rank",
##        print arr
                

if __name__=="__main__":
    main()
