def solution(my_string, num1, num2):
    answer = my_string
    change = ''
    result = list(map(str, my_string))
    for i in range(len(my_string)):
        if i == num1:
            result[i] = answer[num2]
            change +=  result[i]
        elif i == num2:
            result[i] = answer[num1]
            change +=  result[i]
        else:
            change +=  answer[i]
    
    return change

print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))


def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]
    return ''.join(answer)


print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))


# def solution(my_string, num1, num2):
#     answer = my_string
#     answer[num1], answer[num2] = answer[num2], answer[num1]
#     return answer


# print(solution("hello", 1, 2))
# print(solution("I love you", 3, 6))    => 왜 안되는지?