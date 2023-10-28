def solution(s):
    answer = 0
    my_list = s.split()
    answer = int(my_list[0])
    for j in range(1, len(my_list)):
        if my_list[j].isdigit():
            answer += int(my_list[j])
        elif my_list[j].isalpha():
            answer -= int(my_list[j-1])
        elif int(my_list[j]) < 0:   ## isdigit의 함정 정수를 판별해주는 줄 알았으나 양수만 판별가능함. 
            answer += int(my_list[j])
    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))
