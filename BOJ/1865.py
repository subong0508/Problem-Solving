import sys

input = sys.stdin.readline

INF = int(1e9)

def bfs(n, edges):
    distance = [INF] * (n+1)
    distance[1] = 0
    for i in range(n):
        # 모든 간선 확인
        for s, e, t in edges:
            # 현재 간선을 거쳐서 가는 경우가 기존 거리보다 거리가 짧다면
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                # 음수 사이클 존재
                if i == n-1:
                    return True
    return False

tc = int(input())
res = []
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    if bfs(n, edges):
        res.append("YES")
    else:
        res.append("NO")

print(*res, sep='\n')