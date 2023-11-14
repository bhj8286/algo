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


# def solution(rsp):
#     answer = ''

#     rsp_dict = {
#         '2': '0',
#         '0': '5',
#         '5': '2',
#     }

#     for char in rsp:
#         answer += rsp_dict[char]

#     return answer