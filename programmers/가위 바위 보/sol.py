def solution(rsp):
    answer = ''
    for k in rsp:
        if k == '0':
            answer += '5'
            
        elif k == '2':
            answer += '0'
            
        elif k == '5':
            answer += '2'
            
           
    return answer

print(solution('2'))
print(solution('205'))