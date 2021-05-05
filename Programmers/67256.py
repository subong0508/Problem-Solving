def calc_dist(loc1, loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    for n in numbers:
        if n in (1, 4, 7):
            left = [n//3, 0]
            answer += 'L'
        elif n in (3, 6, 9):
            right = [n//3-1, 2]
            answer += 'R'
        else:
            if n == 0:
                n = 10
            loc = [n//3, 1]
            dist_l = calc_dist(left, loc)
            dist_r = calc_dist(right, loc)
            if dist_l == dist_r:
                if hand == 'left':
                    left = loc
                    answer += 'L'
                else:
                    right = loc
                    answer += 'R'
            else:
                if dist_l < dist_r:
                    left = loc
                    answer += 'L'
                else:
                    right = loc
                    answer += 'R'
    return answer