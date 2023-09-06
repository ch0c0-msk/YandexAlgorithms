def isListGrow(seq):
    prev = seq[0]
    for i in range(1,len(seq)):
        if seq[i] <= prev:
            return False
        else:
            prev = seq[i]
    return True
seq = input().split(' ')
if isListGrow(seq):
    print("YES")
else:
    print("NO")