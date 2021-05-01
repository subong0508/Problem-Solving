from collections import deque

n, m, v = map(int, input().split())

graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for i in range(n+1):
    graph[i] = sorted(graph[i])

def dfs(i, visited, graph, stack):
    if visited[i]:
        return
    visited[i] = True
    stack.append(i)
    for j in graph[i]:
        dfs(j, visited, graph, stack)

def bfs(start, visited, graph, stack):
    q = deque([start])
    visited[start] = True
    while q:
        i = q.popleft()
        stack.append(i)
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                q.append(j)

visited = [False] * (n+1)
stack = []
dfs(v, visited, graph, stack)
print(*stack, sep=' ')

visited = [False] * (n+1)
stack = []
bfs(v, visited, graph, stack)
print(*stack, sep=' ')