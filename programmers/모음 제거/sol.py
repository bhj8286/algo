def solution(my_string):
    answer = ''
    mouem = ['a', 'e', 'i', 'o', 'u'] 
    for i in my_string:
        if i not in mouem:
            answer += i
        elif i in mouem:
            continue
    return answer





print(solution("bus"))
print(solution("nice to meet you"))