def solution(age):
    answer = str(age)
    result = ''
    age_dict = {
        '0' : 'a',
        '1' : 'b',
        '2' : 'c',
        '3' : 'd',
        '4' : 'e',
        '5' : 'f',
        '6' : 'g',
        '7' : 'h',
        '8' : 'i',
        '9' : 'j'
    }
    for i in answer:
        result += age_dict[i]
    return result

print(solution(23))
print(solution(51))
print(solution(100))