def solution(my_string):
    answer = ''
    my_string_list = []
    result = ''
    for i in my_string:
        if i.isupper() == True:
           answer += i.lower()
        else:
            answer += i
    for j in answer:
        my_string_list.append(j)
        my_string_list.sort()
    for k in my_string_list:
        result += k


    return result




print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))


## def solution(my_string):
    # return ''.join(sorted(my_string.lower()))  ->훨씬 간단한 풀이..