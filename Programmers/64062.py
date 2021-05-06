def possible(val, stones, k):
    stones_ = [max(s-val+1, 0) for s in stones]
    zeros = 0
    for s in stones_:
        if s > 0:
            zeros = 0
        else:
            zeros += 1
            if zeros >= k:
                return False
    return True    

def solution(stones, k):
    answer = 0
    l = 0
    r = max(stones)
    while l <= r:
        mid = (l + r) // 2
        if possible(mid, stones, k):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
    return answer