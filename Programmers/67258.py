def solution(gems):
    n = len(gems)
    m = len(set(gems))
    i = j = 0
    s = {}
    cnt = 0
    answer = [1, n]
    min_diff = n-1
    while i < n:
        while j < n and cnt < m:
            if gems[j] in s:
                s[gems[j]] += 1
            else:
                cnt += 1
                s[gems[j]] = 1
            j += 1
        if (j-(i+1)) < min_diff and cnt == m:
            answer = [i+1, j]
            min_diff = j-(i+1)
        if s[gems[i]] == 1:
            cnt -= 1
            del s[gems[i]]
        else:
            s[gems[i]] -= 1
        i += 1
    return answer