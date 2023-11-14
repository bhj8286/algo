import string
def solution(s):
    answer = []
    my_list = list(map(str,s))
    alphabet_list = [i for i in string.ascii_lowercase] ## 아스키코드를 활용한 소문자 리스트를 출력
    for al in alphabet_list:
        if my_list.count(al) == 1:
            answer.append(al)
        answer.sort()
        result = ''.join(answer)

    return result

print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))

## 내가 작성한 코드를 한 줄 로 적은 것..
# def solution(s):
#     answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
#     return answer