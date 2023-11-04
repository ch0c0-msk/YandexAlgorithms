from heapq import heappop, heappush

def findTicketsNumber(d, students):
    events = []
    START = -1
    END = 1
    for i, s in enumerate(students):
        events.append((s, START, i))
        events.append((s+d, END, i))
    events.sort()
    result = [None]*len(students)
    heap = list(range(1, len(students) + 1))
    maxTicketNumber = 0
    for pos, eventType, idx in events:        
        if eventType == START:
            nextTicketNumber = heappop(heap)
            maxTicketNumber = max(nextTicketNumber, maxTicketNumber)
            result[idx] = nextTicketNumber
        elif eventType == END:
            studentTicketNumber = result[idx]
            heappush(heap, studentTicketNumber)
    return result

def main():
    n, d = map(int, input().split())
    students = [int(i) for i in input().split()]
    result = findTicketsNumber(d, students)
    print(max(result))
    print(*result)

if __name__ == "__main__":
    main()