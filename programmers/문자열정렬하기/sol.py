def solution(my_string):
    answer = []
    for i in my_string:
        if i in list(map(str, range(0,10))):
            answer.append(int(i))
        else:
            continue
        answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))