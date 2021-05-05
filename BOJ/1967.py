import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def dijkstra(start, tree):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0
    h = [(0, start)]
    while h:
        cost, now = hq.heappop(h)
        if distance[now] < cost:
            continue
        for node, c in tree[now]:
            if cost + c < distance[node]:
                distance[node] = cost + c
                hq.heappush(h, (distance[node], node))
    return distance

distance = dijkstra(1, tree)
max_node = distance.index(max(distance[1:]))
answer = max(dijkstra(max_node, tree)[1:])

print(answer)