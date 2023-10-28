# 처음 작성한 코드 
# def solution(letter):
#     answer = ''
#     morse = { 
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'
# }
#     for i in answer:  -->  answer+= morse[i] KeyError: ' '가 떴는데 morse에서 문자열로 인식을 하지않는듯? 자세한 건 질문해야할듯 
                                                        # 그래서 후에 split()으로 띄어쓰기기준으로 쪼개고 나서 반복문 실행함
#         answer+= morse[i]
            
#     return answer


# print(solution(".... . .-.. .-.. ---"))
# print(solution(".--. -.-- - .... --- -."))

def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    morse_code = letter.split()
    for code in morse_code:
        if code in morse:
            answer+= morse[code]
            
    return answer


print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))