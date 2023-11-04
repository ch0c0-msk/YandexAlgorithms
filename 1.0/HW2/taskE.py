def findPlayerPlace(n, seq):
    winnerThrow = seq[0]
    winnerWasBefore = True
    playerBestThrow = None
    for i in range(1, len(seq) - 1):
        if seq[i] > winnerThrow:
            winnerThrow = seq[i]
            winnerWasBefore = True
            playerBestThrow = None
        else:
            if winnerWasBefore:
                if seq[i] % 10 == 5 and seq[i+1] < seq[i]:
                    if playerBestThrow is None or playerBestThrow < seq[i]:
                        playerBestThrow = seq[i]
    
    if not playerBestThrow:
        return 0
    
    res = 1
    for item in seq:
        if item > playerBestThrow:
            res += 1
    
    return res

def main():
    n = int(input())
    seq = [int(i) for i in input().split()]
    print(findPlayerPlace(n, seq))

if __name__ == "__main__":
    main()