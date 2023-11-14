def solution(n, t):
    answer = (n*2) * 2**(t-1)
    return answer


print(solution(2, 10))
print(solution(7, 15))