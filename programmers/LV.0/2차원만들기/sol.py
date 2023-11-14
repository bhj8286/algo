def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        result = [] 
        for j in range(n):
            result.append(num_list[i+j])
                  
        answer.append(result)            
        
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8],2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))

## 내가 구현하고자 했던 코드의 이상적인 모습
# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):
#         answer.append(num_list[i:i+n])  --> num_list의 인덱스값을 구간으로 자를 수 있다는 사실을 몰랐다
#     return answer