def solution(num, total):
    answer = []
    num_list = list(range(-500, 1000))
    for i in range(1001):
        if sum(num_list[i:i+num]) == total:
            answer = num_list[i:i+num]
            break
    return answer

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))

# 첫 풀이:
# def solution(num, total):
#     answer = []
#     num_list = list(range(-2, 10000))  ##-> 범위 설정이 잘못된듯하다
#     for i in range(501):              ## -> 역시 범위 설정이 잘못된 듯 범위들만 수정하니까 바로 통과함
#         if sum(num_list[i:i+num]) == total:
#             answer = num_list[i:i+num]
#             break
#     return answer

# print(solution(3, 12))
# print(solution(5, 15))
# print(solution(4, 14))
# print(solution(5, 5))