import math

def main():
    xA, yA, xB, yB = map(int, input().split())
    print("{0:.12f}".format(findShortestWay((xA, yA), (xB, yB))))

def findShortestWay(a, b):

    routeLength = 0

    rA = findCenterDistance(a)
    rB = findCenterDistance(b)

    routeLength += abs(rA - rB)
    
    angle = math.atan2(a[1], a[0]) - math.atan2(b[1], b[0])

    routeLength += abs(angle) * min(rA, rB)

    return min(routeLength, rA + rB)

def findCenterDistance(point):
    return math.sqrt(point[0]**2 + point[1]**2)

if __name__ == "__main__":
    main()