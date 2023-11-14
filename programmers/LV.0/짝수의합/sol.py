# def solution(n):
#     answer = 0  -> answer 이라는 변수를 생성한 것

#     numbers = range(1, n+1)
     
#     for number in numbers:
#         if number % 2 == 0:
#             answer = answer + number
#     return answer
               

# print(solution(10))
# print(solution(4))

def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)

print(solution(10))
print(solution(4))

# def solution(n):

#     numbers = range(1, n+1)
    #   result = []
     
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return sum(result)
               

# print(solution(10))
# print(solution(4))