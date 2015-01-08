price = [2048,1024,512,256,128,64,32,16,8,4,2,1]
 
def rcpt():
    p = int(raw_input())
    number_of_menus = 0
    pCounter = 0
    while p!=0:
        if p>=price[pCounter]:
            p-= price[pCounter]
            number_of_menus+=1
        else:
            pCounter+=1
    return number_of_menus
 
def main():
    t = int(raw_input())
    for i in range(t):
        print rcpt()
 
if __name__=="__main__":
    main() 
