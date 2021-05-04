import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
a, b = map(int, input().split())

def dijkstra(start, graph):
    INF = int(1e9)
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

print(dijkstra(a, graph)[b])