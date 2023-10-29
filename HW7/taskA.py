def findStudentsCount(n, observedList):
    events = []
    SEGMENT_START = -1
    SEGMENT_END = 1
    for start, end in observedList:
        events.append((start, SEGMENT_START))
        events.append((end, SEGMENT_END))
    events.sort()
    result = n
    currentSegmentsCount = 0
    left = 0
    for pos, eventType in events:
        if eventType == SEGMENT_START:
            if currentSegmentsCount == 0:
                left = pos
            currentSegmentsCount += 1
        if eventType == SEGMENT_END:
            currentSegmentsCount -= 1
            if currentSegmentsCount == 0:
                result -= (pos - left + 1)
    return result

def main():
    n, m = map(int, input().split())
    observedList = [map(int, input().split()) for _ in range(m)]
    print(findStudentsCount(n, observedList))
if __name__ == "__main__":
    main()