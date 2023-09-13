def findMaxDigitsByMul(seq):
    maxPos1 = None
    maxPos2 = None
    minNeg1 = None
    minNeg2 = None
    for i in range(len(seq)):
        if seq[i] >= 0:
            if maxPos1 is None or seq[i] > maxPos1:
                maxPos2 = maxPos1
                maxPos1 = seq[i]
            elif maxPos2 is None or seq[i] > maxPos2:
                maxPos2 = seq[i]
        else:
            if minNeg1 is None or seq[i] < minNeg1:
                minNeg2 = minNeg1
                minNeg1 = seq[i]
            elif minNeg2 is None or seq[i] < minNeg2:
                minNeg2 = seq[i]
    
    if (maxPos1 is not None and maxPos2 is not None) or (minNeg1 is not None and minNeg2 is not None):
        if (maxPos1 is not None and minNeg1 is not None):
            if maxPos1 * maxPos2 > minNeg1 * minNeg2:
                return maxPos2, maxPos1
            else:
                return minNeg1, minNeg2
        else:
            if maxPos1 is not None:
                return maxPos2, maxPos1
            else:
                return minNeg1, minNeg2
    else:
        return minNeg1, maxPos1

def main():
    seq = [int(i) for i in input().split()]
    for item in findMaxDigitsByMul(seq):
        print(item, end=" ") 
    
if __name__ == "__main__":
    main()