def findRisesLength(points, tracks):
    prefixLeftToRight, prefixRightToLeft = createPrefixSum(points)
    result = []
    for track in tracks:
        if track[0] < track[1]:
            result.append(prefixLeftToRight[track[1] - 1] - prefixLeftToRight[track[0] - 1])
        else:
            result.append(prefixRightToLeft[track[1] - 1] - prefixRightToLeft[track[0] - 1])
    return result

def createPrefixSum(points):
    prefixLeftToRight = [0] + [None]*(len(points) - 1)
    prefixRightToLeft = [None]*(len(points) - 1) + [0]
    for i in range(1, len(points)):
        prefixLeftToRight[i] = prefixLeftToRight[i-1] + max(points[i][1] - points[i-1][1], 0)
        prefixRightToLeft[len(points) - i - 1] = prefixRightToLeft[len(points) - i] + max(points[len(points) - i - 1][1] - points[len(points) - i][1], 0)
    return prefixLeftToRight, prefixRightToLeft

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    tracks = [tuple(map(int, input().split())) for _ in range(m)]
    result = findRisesLength(points, tracks)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()