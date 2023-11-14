def solution(n):
    answer = 0
    result = 1
    for i in range(1, n+1):
        result = result*i 
        if result > n:
            break
        answer = i
        
    return answer


print(solution(3628800))
print(solution(7))

# def solution(n):
#     answer = 0
#     result = 1
#     for i in range(1, n): --> 범위설정 실패 n이 1이면 답이 1이 아니라 0이 나와버림
#         result = result*i 
#         if result > n:
#             break
#         answer = i
        
#     return answer


# print(solution(3628800))
# print(solution(7))