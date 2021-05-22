import sys
import heapq

input = sys.stdin.readline
t = int(input())
res = []
for _ in range(t):
    min_heap = []
    max_heap = []
    visited = {}
    k = int(input())
    for _ in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            visited[num] = visited.get(num, 0) + 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1:
                while max_heap:
                    val = -1 * heapq.heappop(max_heap)
                    if visited[val] > 0:
                        visited[val] -= 1
                        break
            else:
                while min_heap:
                    val = heapq.heappop(min_heap)
                    if visited[val] > 0:
                        visited[val] -= 1
                        break
    min_val = float("Inf")
    max_val = -float("Inf")
    found = False
    for num, val in visited.items():
        if val > 0:
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            found = True
    if found:
        res.append(str(max_val) + ' ' + str(min_val))
    else:
        res.append("EMPTY")

print(*res, sep='\n')