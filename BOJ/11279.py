import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []
res = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h, -x)
    else:
        if not h:
            res.append(0)
        else:
            res.append(-heapq.heappop(h))

print(*res, sep='\n')