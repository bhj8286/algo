def solution(box, n):
    answer = 1
    for i in range(len(box)):
        a = box[i] // n
        answer *= a
    return answer



print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))