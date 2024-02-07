# Task condition: https://contest.yandex.ru/contest/53031/problems/C/

import math, heapq

def createAdjacensyList(n, k):
    res = [list() for _ in range(n+1)]
    for i in range(k):
        a, b, l = map(int, input().split())
        res[a].append((b, l))
        res[b].append((a, l))
    return res

def findShortestPath(adjList, dep, dest):
    n = len(adjList)
    heap = list()
    distList = [math.inf]*n
    markedList = [False]*n
    distList[dep] = 0
    heapq.heappush(heap, (distList[dep], dep))
    while len(heap) != 0:
        curElem = heapq.heappop(heap)
        curNode = curElem[1]
        curDist = curElem[0]
        if markedList[curNode] == False:
            markedList[curNode] = True
            for i in range(len(adjList[curNode])):
                curPath = curDist + adjList[curNode][i][1]
                if curPath < distList[adjList[curNode][i][0]]:
                    distList[adjList[curNode][i][0]] = curPath
                    heapq.heappush(heap, (curPath, adjList[curNode][i][0]))
    res = -1
    if not math.isinf(distList[dest]):
        res = distList[dest]
    return res

def main():
    n, k = map(int, input().split())
    adjList = createAdjacensyList(n, k)
    a, b = map(int, input().split())
    print(findShortestPath(adjList, a, b))

if __name__ == "__main__":
    main()