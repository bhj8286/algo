def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower() == True:
          answer += i.upper()
        elif i.islower() == False:
           answer += i.lower()
    return answer

print(solution("cccCCC"))
print(solution("abCdEfghIJ"))