def solution(common):
    answer = 0
    for i in range(0,1):
        if common[i+1] - common[i] == common[i+2]-common[i+1]:
            answer = common[-1] + (common[i+1] - common[i])
        elif common[i+1] // common[i] == common[i+2] // common[i+1]:
            answer = common[-1] * (common[i+1] // common[i])
    return answer


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))