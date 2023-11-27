from string import ascii_lowercase
from string import ascii_uppercase
def solution(s, n):
    answer = ''
    # 알파벳 대소문자 각각 리스트로 생성, 한 번 더 반복한 이유: w,x,y,z .. 등등 뒤 알파벳들을 n만큼 밀었을 때 out of range 발생 방지
    alpha_list = list(ascii_lowercase)+list(ascii_lowercase) 
    Alpha_list = list(ascii_uppercase)+list(ascii_uppercase)
    for i in s:
        # i가 대문자인지 소문자인지 공백인지 판별 
        # i가 있는 리스트에서 n만큼 뒤에 있는 알파벳 출력, 무조건 앞에서 한 번 나온 요소의 인덱스를 뽑아주는 index 활용
        if i.isupper():
            i = Alpha_list[Alpha_list.index(i)+n] 
            answer += i
        elif i.islower():
            i = alpha_list[alpha_list.index(i)+n]
            answer += i
        elif i == ' ':
            answer += ' '
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))