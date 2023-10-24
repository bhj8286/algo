def solution(n):
    answer = 0
    a, b = divmod(n, 7)
    if b == 0:
        answer += a
    elif 1 <= b < 7:
        answer += a+1
    return answer

print(solution(7))
print(solution(1))
print(solution(15))