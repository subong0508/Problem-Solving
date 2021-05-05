n = int(input())
graph = [[] for _ in range(n+1)]
e = int(input())
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i, graph, visited):
    if visited[i]:
        return
    visited[i] = True
    for j in graph[i]:
        dfs(j, graph, visited)

visited = [False] * (n+1)

dfs(1, graph, visited)

print(sum(visited)-1)