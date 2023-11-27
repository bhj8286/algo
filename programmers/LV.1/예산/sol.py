def solution(d, budget):
    answer = 0
    if sum(d) == budget: # 리스트 합이 예산과 같다면 바로 리스트 길이 출력 
        answer = len(d)
    elif sum(d) != budget:
        new = sorted(d) # d를 오름차순으로 정렬
        check = []
        for i in new: # 정렬된 리스트에서 요소를 하나씩 꺼내온다 
            if sum(check) <= budget:
                check.append(i)   
                answer = len(check)
                if sum(check) > budget:
                    check.pop()
                    answer = len(check)
                    break
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))