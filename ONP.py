def RPN():
    exp = raw_input()
    stack = []
    output = ""
    for char in exp:
        if char not in "+-/*()^":
            output+=char
        else:
            if char!=")":
                stack.append(char)
            else:
                while True:
                    c = stack.pop()
                    if c=="(":
                        break
                    else:
                        output+=c
    return output

def main():
    t = int(raw_input())
    for i in range(t):
        print RPN()

if __name__ == "__main__":
    main()
