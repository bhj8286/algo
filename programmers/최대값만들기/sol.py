def solution(numbers):
    answer = 0
    numbers.sort()
   
    answer = int(numbers[-1]) * int(numbers[-2])
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))



# def solution(numbers):
#     answer = 0
#     List = []
#     List = numbers.sort()
#     answer = int(List[-1]) * (List[-2])
#     return answer

# print(solution([1, 2, 3, 4, 5]))
# print(solution([0, 31, 24, 10, 1, 9]))  => 결과가 출력되지않는다 스터디에서 같이 얘기해보면 좋을듯