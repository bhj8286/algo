def solution(array, n):
    answer = 0
    min_num = 10000000000
    array.sort()
    for number in array:
        if abs(n-number) < min_num:
            min_num = abs(n-number)
            answer = number
        elif abs(n-number) == min_num:
            answer = answer
        
    return answer

print(solution([3, 10, 28],20))
print(solution([10, 11, 12],13))
## 주의점 : 더 작은 수를 출력하게 하기 위해 for문을 돌리기 전에 array를 오름차순으로 정렬해준 후 elif문에서 n과 number의 차가 같은 경우 
## answer을 그대로 answer로 두어 더 작은 수를 출력하게 하였다