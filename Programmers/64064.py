def possible(id1, id2):
    if len(id1) != len(id2):
        return False
    n = len(id1)
    for i in range(n):
        if id1[i] != id2[i] and id2[i] != '*':
            return False
    return True

def dfs(i, s, user_id, banned_id):
    if i == len(banned_id):
        tmp = ''.join(sorted(s))
        answer.add(tmp)
        return 
    candidates = [u_id for u_id in user_id if u_id not in s and possible(u_id, banned_id[i])] 
    for c in candidates:
        s.add(c)
        dfs(i+1, s, user_id, banned_id)
        s.remove(c)
            
def solution(user_id, banned_id):
    global answer
    answer = set()
    dfs(0, set(), user_id, banned_id)
    return len(answer)