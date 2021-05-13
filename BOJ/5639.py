import sys

sys.setrecursionlimit(10 ** 5)

post = []
for i in range(10000):
    try:
        tmp = int(input())
        post.append(tmp)
    except:
        break

n = len(post)
visited = set()

def solution(start, end):
    if start > end:
        return
    div = end+1
    for i in range(start+1, end+1):
        if post[i] > post[start]:
            div = i
            break
    solution(start+1, div-1)
    solution(div, end)
    print(post[start])

solution(0, n-1)