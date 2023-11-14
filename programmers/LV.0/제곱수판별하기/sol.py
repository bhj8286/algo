import math
def solution(n):
    answer = 0
    number = math.sqrt(n) 
    if int(number) == number:
        answer = 1
    elif int(number) != number:
        answer = 2
    else:
        pass
    
    return answer


print(solution(144))
print(solution(976))