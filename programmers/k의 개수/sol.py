def solution(i, j ,k):
    answer = 0
    
    for number in range(i, j+1):
        j_list = [] 
        j_list.extend(str(number)) ## 만약 'apple'을 리스트에 넣을 때 append이용시 ['apple'], extend이용시 ['a','p','p','l','e']로 들어감
        answer += j_list.count(str(k)) ## 리스트이름.count(기준 요소) --> 기준 요소가 리스트안에 몇 개 있는지 카운트해준다
        j_list.clear()
        
        
    return answer


print(solution(1,13,1))
print(solution(10,50,5))
print(solution(3,10,2))