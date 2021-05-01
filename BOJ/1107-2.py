n = int(input())
m = int(input())
broken = []
if m > 0:
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
    channels[i] = min(channels[i], abs(i-100))
    
for i in range(MAX+1):
    channels[n] = min(channels[n], channels[i]+abs(i-n))

print(channels[n])