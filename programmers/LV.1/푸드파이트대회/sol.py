def solution(food):
    answer = ''
    total = ''
    for i,j in enumerate(food[1:]):
        if j >= 2:
            k = j // 2
            total += str(i+1) * k
        else:
            continue
    answer += '0'

    for i in total[::-1]:
        answer += i
        
    answer = total + answer
    
    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))