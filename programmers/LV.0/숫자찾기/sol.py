def solution(num, k):
    answer = 0
    list = []
    for i in str(num):
        list.append(int(i))

    for idx, value in enumerate(list):
        if k == value:
            answer = idx +1 
            break
        else:
            answer = -1
    return answer


print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))