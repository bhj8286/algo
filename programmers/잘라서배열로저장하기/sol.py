def solution(my_str, n):
    answer = []
    for num in range(0,len(my_str),n):
        answer.append(my_str[num:num+n]) ##문자열 슬라이싱을 이용하였다. for문과 문자열의 인덱스값 범위 설정에서 시행착오가 있었음
        
    return answer


print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))