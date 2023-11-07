def solution(array):
    answer = 0
    count = 0
    for i in range(0, max(array)+1):  # 범위는 1000까지인데 다 돌리기엔 런타임을 고려 안할 수가 없었다. 그래서 그냥 리스트의 최댓값까지만 돌리기로 설정
        k = array.count(i)
        if k > count:
            count = k
            answer = i
        elif k == count:
            answer = -1
    return answer

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))