n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = arr[0]
for i in range(1, n):
    arr[i] += arr[i-1]
    answer += arr[i]

print(answer)