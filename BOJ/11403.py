n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF 

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] != INF:
            graph[i][j] = 1
        else:
            graph[i][j] = 0
            
for i in range(n):
    print(*graph[i])