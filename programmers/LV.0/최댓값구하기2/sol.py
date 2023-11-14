# def solution(numbers):
#     numbers.sort(reverse=True)
#     max_num = 0
#     for i in range(1, len(numbers)):
#         if max_num < numbers[i-1] * numbers[i]:
#             max_num = numbers[i-1] * numbers[i]
#         else: 
#             max_num = max_num

#     return max_num

# print(solution([1, 2, -3, 4, -5]))
# print(solution([0, -31, 24, 10, 1, 9]))
# print(solution([10, 20, 30, 5, 5, 20, 5])) ## 91.5점 뜸ㅜ

def solution(numbers):
    numbers.sort(reverse=True)
    max_num = 0
    for i in range(0, len(numbers)):
        if max_num < abs(numbers[i-1]) * abs(numbers[i]):
            max_num = numbers[i-1] * numbers[i]
        else: 
            pass

    return max_num

print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5])) # 이건 통과함..