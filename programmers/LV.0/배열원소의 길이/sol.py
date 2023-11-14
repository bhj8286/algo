def solution(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer



print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))