def findSquare(a1, b1, a2, b2):
    variants = []
    variants.append((a1 + a2) * max(b1, b2))
    variants.append((a1 + b2) * max(a2, b1))
    variants.append((b1 + b2) * max(a1, a2))
    variants.append((b1 + a2) * max(a1, b2))
    if min(variants) == variants[0]:
        return [a1+a2, max(b1, b2)]
    elif min(variants) == variants[1]:
        return [a1+b2, max(a2, b1)]
    elif min(variants) == variants[2]:
        return [b1+b2, max(a1, a2)]
    else:
        return [b1+a2, max(a1, b2)]
    
a1, b1, a2, b2 = map(int, input().split())
for i in findSquare(a1, b1, a2, b2):
    print(i, end = " ")