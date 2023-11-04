def main():
    seq = [int(i) for i in input().split()]
    negMax1 = 0
    negMax2 = 0
    posMax1 = -1
    posMax2 = -1
    posMax3 = -1
    
    for i in seq:
        if i >= 0:
            if i > posMax1:
                posMax3 = posMax2
                posMax2 = posMax1
                posMax1 = i
            elif i > posMax2:
                posMax3 = posMax2
                posMax2 = i
            elif i > posMax3:
                posMax3 = i
        else:
            if i < negMax1:
                negMax2 = negMax1
                negMax1 = i
            elif i < negMax2:
                negMax2 = i
    
    
if __name__ == "__main__":
    main()