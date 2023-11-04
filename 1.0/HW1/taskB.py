def isTreanglePossible(a, b ,c):
    if a < (b+c) and b < (a+c) and c < (a+b) and a > 0 and b > 0 and c > 0:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())



if isTreanglePossible(a, b, c):
    print("YES")
else:
    print("NO")