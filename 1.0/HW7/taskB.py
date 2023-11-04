def findSegmentsCount(segments, points):
    SEGMENT_START = -1
    SEGMENT_END = 1
    POINT = 0
    events = []
    for segment in segments:
        sortedSegment = sorted(segment)
        events.append((sortedSegment[0], SEGMENT_START))
        events.append((sortedSegment[1], SEGMENT_END))
    for i, p in enumerate(points):
        events.append((p, POINT, i))
    events.sort()
    currentSegmentsCount = 0
    result = [0]*len(points)
    for event in events:
        if event[1] == SEGMENT_START:
            currentSegmentsCount += 1
        elif event[1] == POINT:
            result[event[2]] = currentSegmentsCount
        elif event[1] == SEGMENT_END:
            currentSegmentsCount -= 1
    return result

def main():
    n, m = map(int, input().split())
    segments = [map(int, input().split()) for _ in range(n)]
    points = [int(i) for i in input().split()]
    print(*findSegmentsCount(segments, points))

if __name__ == "__main__":
    main()