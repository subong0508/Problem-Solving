import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []
res = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    else:
        if not h:
            res.append(0)
        else:
            tup = heapq.heappop(h)
            res.append(tup[1])

print(*res, sep='\n')