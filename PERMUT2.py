def isAmbi(arr):
    temp = []
    for i in range(len(arr)+1):
        temp.append(-1)
    for i in range(1,len(arr)+1):
        temp[arr[i-1]] = i
        #if i!= arr[arr[i-1]-1]:
            #print "not ambiguous"
            #return
    #print "ambiguous"
    #return
    temp.pop(0)
    if temp==arr:
        print "ambiguous"
        return
    else:
        print "not ambiguous"
        return

def main():
    while True:
        n = int(raw_input())
        if n==0:
            break
        arr = []
        arr = map(int,raw_input().split())
        isAmbi(arr)

if __name__=="__main__":
    main()
