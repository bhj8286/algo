def solution(score):
    answer = []
    result = []
    
    for i in score:
        answer.append(sum(i)/len(i))
        
    my_list = sorted(answer, reverse=True)
    
    for num in answer:
        result.append(my_list.index(num)+1)
       
        
    return result



print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))