def solution(my_string):
    answer = ''
    for real in my_string:
        if real not in answer:
            answer += real
        elif real in answer:
            continue
    return answer


print(solution("people"))
print(solution("We are the world"))

