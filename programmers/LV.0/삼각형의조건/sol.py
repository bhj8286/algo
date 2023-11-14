def solution(sides):
    answer = 0
    sides.sort()
    if sides[-1] < sides[-2] +sides[-3]:
        answer = 1
    else:
        answer = 2
    return answer



print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))