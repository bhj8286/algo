def solution(n, k):
    answer = 0
    answer = (12000 * n) + (2000 * k)
    if n // 10 >= 0:
        answer =(12000 * n) + (2000 * k)- ((n // 10) * 2000)
    return answer


print(solution(10, 3))
print(solution(64, 6))