def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    
    return sum(list(map(int, my_string)))

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))

# k = 'i   m    hojin'  
# k = k.split()
# print(k)
# -->결과: ['i', 'm', 'hojin']
# 문자열.split(sep, maxsplit) 함수는 문자열을 maxsplit 횟수만큼 sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들어 줍니다.