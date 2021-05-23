t = int(input())

arr = [0] * 101
arr[1] = arr[2] = arr[3] = 1

for i in range(4, 101):
    arr[i] = arr[i-2] + arr[i-3]

res = []
for _ in range(t):
    n = int(input())
    res.append(arr[n])

print(*res, sep='\n')