n = int(input())
m = int(input())
broken = list(map(int, input().split()))

INF = int(1e9)
MAX = 1000000

channels = [len(str(i)) for i in range(MAX+1)]
for i in range(MAX+1):
    for b in broken:
        if str(b) in str(i):
            channels[i] = INF
channels[100] = 0

for i in range(MAX+1):
    if 0 <= i-1 <= MAX:
        channels[i] = min(channels[i], channels[i-1]+1)
    if 0 <= i+1 <= MAX:
        channels[i] = min(channels[i], channels[i+1]+1)

for i in range(MAX, -1, -1):
    if 0 <= i-1 <= MAX:
        channels[i] = min(channels[i], channels[i-1]+1)
    if 0 <= i+1 <= MAX:
        channels[i] = min(channels[i], channels[i+1]+1)

print(channels[n])