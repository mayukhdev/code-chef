def numgame():
    n = int(raw_input())
    if n%2==0:
        return "ALICE"
    else:
        return "BOB"

def main():
    t = int(raw_input())
    for i in range(t):
        print numgame()

if __name__ == "__main__":
    main()
