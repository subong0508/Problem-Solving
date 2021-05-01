import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
distance = [[INF] * (n+1) for _ in range(n+1)]

def dijkstra(start):
    h = []
    distance[start][start] = 0
    heapq.heappush(h, (start, 0))
    while h:
        i, cost = heapq.heappop(h)
        if distance[start][i] < cost:
            continue
        for j in graph[i]:
            if cost+1 < distance[start][j]:
                distance[start][j] = cost+1
                heapq.heappush(h, (j, distance[start][j]))

for i in range(1, n+1):
    dijkstra(i)

min_idx = -1
res = int(1e9)
for i in range(1, n+1):
    tmp = sum(distance[i][1:])
    if tmp < res:
        min_idx = i
        res = tmp

print(min_idx)