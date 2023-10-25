def solution(n):
    answer = []
    for i  in range(1,n+1):
        if n % i == 0:
            answer.append(i)
        elif n % i != 0:
            continue
    return answer


print(solution(24))
print(solution(29))