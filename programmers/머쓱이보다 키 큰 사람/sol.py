def solution(array, height):
    answer = []
    for k in array:
        if k > height:
            answer.append(k)
    return len(answer)


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))