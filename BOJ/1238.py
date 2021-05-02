import sys
import heapq as hq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph1[a].append((b, t))
    graph2[b].append((a, t))

def dijkstra(start, graph):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0
    h = [(start, 0)]
    while h:
        now, cost = hq.heappop(h)
        if distance[now]  < cost:
            continue
        for node, dist in graph[now]:
            if cost + dist < distance[node]:
                distance[node] = cost + dist
                hq.heappush(h, (node, distance[node]))
    return distance

distance1 = dijkstra(x, graph1)
distance2 = dijkstra(x, graph2)
distance = [d1+d2 for d1, d2 in zip(distance1, distance2)]

answer = 0
for i in range(1, n+1):
    if distance[i] > answer:
        answer = distance[i]

print(answer)