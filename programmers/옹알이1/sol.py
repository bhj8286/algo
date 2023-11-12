# 풀이 과정: 직접 파이썬 튜터로 돌리면서 보여주는게 이해가 더 빠를 것같다 
def solution(babbling):
    answer = 0
    baebae = ["aya", "ye", "woo", "ma"]  # 아기가 발음할 수 있는 것들을 리스트로 따로 작성 
    check_list=[]
    for i in babbling:
        for j in baebae:   # => 반복문 실행 
            if j in i:
                k = i.replace(j,'_') # => 바로 ''으로 바꾸지 않고 '_'을 넣은 이유: 공백으로 치환시 연속되지 않았던 문자들이 붙게되어 발음할 수 있게 되는 경우 존재  
                i = k
                if i.replace('_','') == '': # 치환을 한 후 최종적으로 '_'를 ''으로 바꿔 주어 판단한다
                    check_list.append(i)  # 최종적으로 공백인 것들을 체크리스트에 넣어줌
    answer = len(check_list) # 갯수를 판단해야하므로 리스트의 길이 출력

    
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))