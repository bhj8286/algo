def solution(message):
    answer = 0
    result = []
    for m in message:
        result.append(m)
        answer = 2 * len(result)
    return answer




print(solution("happy birthday!"))
print(solution("I love you~"))