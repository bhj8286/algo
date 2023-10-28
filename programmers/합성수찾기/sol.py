def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i <= 3:
            continue
        elif i % 2 ==0 or (n**0.5)==int(n**0.5) or i % 3 == 0:
            answer += 1   
        elif i >= 10 and i % 5 ==0:
            answer += 1
    return answer

print(solution(10))
print(solution(15)) # 반례가 있는 듯 ex)77
 
def solution(n):
    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count >= 1:
            answer += 1
    return answer
print(solution(10))
print(solution(15))  #