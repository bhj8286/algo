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
