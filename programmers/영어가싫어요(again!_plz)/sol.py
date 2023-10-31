def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])  ##문자열을 바꿔주는 replace 활용!

    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))