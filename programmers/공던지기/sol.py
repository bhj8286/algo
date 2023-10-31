## 내 풀이: 공은 한명 건너 뛰어 던진다는 것은 같은 리스트를 연장시켜 계산하면 된다고 생각하였기에 num_list를 만듦 
## 건너 뛰기때문에 간격을 2, 간격이 두배가 되었기 때문에 범위는 k*2전까지(공을 받는 사람이 아닌 공은 던진 사람을 찾기 때문에 k*2전까지로 설정 ) 
## 따라서 range(0, k*2, 2)로 설정
def solution(numbers, k):
    answer = 0
    thrower = 0
    num_list = [] 
    for i in range(k):
        num_list.extend(numbers)   
    for j in range(0,k*2,2):
        thrower = num_list[j]
        
    return thrower


print(solution([1, 2, 3, 4],2))
print(solution([1, 2, 3, 4, 5, 6],5))
print(solution([1, 2, 3],3))




def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)] # 너무 깔끔하게 잘 풀어서 참고용






# def solution(numbers, k):
#     answer = 0
#     num_list = numbers
#     for i in range(k):
#         numbers.extend(num_list)  -> num_list와 numbers에 모두 숫자가 더해지는 데 numbers는 왜 바뀌는지?
#     print(numbers)
        
#     return answer


# print(solution([1, 2, 3, 4],2))
# print(solution([1, 2, 3, 4, 5, 6],5))
# print(solution([1, 2, 3],3))