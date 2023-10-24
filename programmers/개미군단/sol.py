# def solution(hp):
#     answer = 0

#     a, b = divmod(hp, 5)
#     hp = b
#     answer += a
    
#     a, b = divmod(hp, 3)
#     hp = b
#     answer += a

#     answer += hp

#     return answer


# print(solution(23))
# print(solution(24))
# print(solution(999))



def solution(hp):
    answer = 0
    a,b = divmod(hp, 5)
    answer += a
    c,d = divmod(b, 3)
    answer += c
    e = d // 1
    answer += e
    return answer



print(solution(23))
print(solution(24))
print(solution(999))
