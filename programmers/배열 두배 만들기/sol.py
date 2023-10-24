def solution(numbers):
    answer = []
    for num in range(len(numbers)):
        answer.append(numbers[num]*2)
    return answer



print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))