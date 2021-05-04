import sys
import heapq as hq

input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())
k = int(input())
edges = {}
for _ in range(e):
    u, v, w = map(int, input().split())
    edges[(u, v)] = min(edges.get((u, v), INF), w)

graph = [[] for _ in range(n+1)]
for (u, v), w in edges.items():
    graph[u].append((v, w))

def dijkstra(start, graph):
    distance = [INF] * (n+1)
    distance[start] = 0
    h = [(0, start)]
    while h:
        cost, now = hq.heappop(h)
        if distance[now] < cost:
            continue
        for node, c in graph[now]:
            if cost + c < distance[node]:
                distance[node] = cost + c
                hq.heappush(h, (distance[node], node))
    return distance

distance = dijkstra(k, graph)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])