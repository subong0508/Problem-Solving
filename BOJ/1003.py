t = int(input())

zeros = [1, 0]
ones = [0, 1]

for _ in range(40):
    zeros.append(zeros[-2] + zeros[-1])
    ones.append(ones[-2] + ones[-1])

for _ in range(t):
    n = int(input())
    print(zeros[n], ones[n])