def solution(emergency):
    answer = []
    array = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(array.index(i)+1) ## 리스트이름.index -> 리스트의 인덱스 추출 가능
    return answer


print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))