def solution(slice, n):
    answer = 0
    a, b = divmod(n, slice)
    if b == 0:
        answer += a
    elif 1 <= b < slice:
        answer += a+1
    return answer

print(solution(7, 10))
print(solution(4, 12))