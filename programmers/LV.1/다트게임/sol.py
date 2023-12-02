# 내 풀이
def solution(dartResult):
    answer = []
    # 띄어쓰기를 기준으로 나누고 eval할거라 아래와 같이 치환
    dartResult = dartResult.replace('*', 'k ') # 나중에 헷갈리거나 반복문 돌릴 때 쉽게 인식하기 위해 임의로 조정  
    dartResult = dartResult.replace('#', '# ')
    # 문제 풀이 메커니즘 생각부터 eval을 염두하고 시작했기에 다음과 같이 치환
    dartResult = dartResult.replace('S', '**1 ') 
    dartResult = dartResult.replace('D', '**2 ')
    dartResult = dartResult.replace('T', '**3 ')
    dartResult = dartResult.split()
    point = []
    for i in dartResult:
        if i == '#' or i == 'k': # 그냥 문자만 있는 경우 eval로 처리가 불가능, 그대로 다시 append 
            i = i
            point.append(i)
        else:
            i = eval(i) # 문자열을 계산해주는 식 
            point.append(i)
    for j in point:
        if str(j).isdigit():
            answer.append(int(j))
        # 별이 첫번째 기회에 나오면 첫 점수만 2배가 된다.
        elif j == 'k' and len(answer) == 1:
            answer[-1] = answer[-1] * 2
        elif j == 'k' and len(answer) > 1: 
            answer[-1] = answer[-1] * 2  
            answer [-2] = answer[-2] * 2
        elif j == '#': # '#'은 전의 점수에만 적용되기에 마지막에 append된 숫자에만 -1을 곱해준다.
            answer[-1] = answer[-1] * -1
    answer = sum(answer)
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

## 도현님 코드인데 re를 import해서 findall()이라는 함수를 쓴 것이 인상적이었음, 알아두면 유용하게 쓰일 듯하다

import re
# 정규 표현식 사용할 때 re 모듈 사용
# 특정 조건의 문자열이나 패턴을 가지는 문자열을 쉽게 처리가능
# 위치를 찾거나, 일치하는 객체를 반환, 분리, 모두 찾기 등이 가능 
def solution(dartResult):
    answer = []
    power = {'S': 1, 'D': 2, 'T': 3}
    # 해당하는 정규표현식의 문자열을 모두찾아 리스트로 반환
    # '\d' 숫자 '+'1번이상 반복되는 패턴, '[S, D, T]' S,D,T가 있는지 찾음, [*, #] 기호 찾음
    # '?' 앞의 패턴이 0번 혹은 1번 표시되는지 
    a = re.findall('\d+[S, D, T][*, #]?', dartResult)
    for i in a:
        # 기호가 있다면 '2D*'과 같은 형식
        if '#' in i or '*' in i:
            # 숫자만 가져와 power 만큼 제곱해준다
            answer.append(int(i[:-2]) ** power[i[-2]])
            # 기호가 #이면
            if i[-1] == '#':
                answer[-1] = answer[-1] * (-1)
            # 기호가 *이고 answer이 2개 이상이면
            elif i[-1] == '*' and len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            # 기호가 *이고 answer이 1개이면
            else:
                answer[-1] = answer[-1] * 2
        # 기호 없으면 제곱만 해서 저장 
        else:
            answer.append(int(i[:-1]) ** power[i[-1]])
    # answer을 모두 합해 반환
    return sum(answer)
