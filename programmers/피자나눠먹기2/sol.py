# import math ## 파이썬에서는 최소공배수를 구하는 함수 제공 
# def solution(n):
#     answer = 0
#     a, b = divmod(n, 6)
#     if b == 0:
#         answer = a
#     elif b != 0:
#         LCM = math.lcm(n, 6)  ## 최소공배수 제공 함수 -> 프로그래머스에선 안먹힘
#         answer = LCM // 6

#     return answer

# print(solution(6))
# print(solution(10))
# print(solution(4)) 

## 최소 공배수 구하는 코드 
# for i in range(max(A,B), (A*B) + 1):
# 	if i % A == 0 and i % B == 0:
# 		print(i)
# 		break



def solution(n):
    answer = 0
    a, b = divmod(n, 6)
    if b == 0:
        answer = a
    elif b != 0:
        for i in range(max(n, 6),(n*6)+1):
            if i % n == 0 and i % 6 == 0:
                answer = i // 6
                break
    return answer

print(solution(6))
print(solution(10))
print(solution(4)) 