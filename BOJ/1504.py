import sys
import heapq as hq

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start, graph):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0
    h = [(start, 0)]
    while h:
        now, cost = hq.heappop(h)
        if distance[now] < cost:
            continue
        for node, c in graph[now]:
            if cost + c < distance[node]:
                distance[node] = cost + c
                hq.heappush(h, (node, distance[node]))
    return distance

distance_start = dijkstra(1, graph)
distance_v1 = dijkstra(v1, graph)
distance_v2 = dijkstra(v2, graph)

answer = int(1e9)
# 1 -> v1 -> v2 -> n
if distance_start[v1] + distance_v1[v2] + distance_v2[n] < answer:
    answer = distance_start[v1] + distance_v1[v2] + distance_v2[n]
# 1 -> v2 -> v1 -> n
if distance_start[v2] + distance_v2[v1] + distance_v1[n] < answer:
    answer = distance_start[v2] + distance_v2[v1] + distance_v1[n]

if answer == int(1e9):
    print(-1)
else:
    print(answer)