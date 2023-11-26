#첫 번째 풀이
def solution(phone_number):
    answer = ''
    pn = ''.join(reversed(phone_number))  ### 거꾸로 돌려버려서 숫자 배열자체가 달라지게 됨
    real_num = []  
    num_list = []
    for _ in pn:
        num_list.append(_)
    real_num = num_list[:4]
    real_num = ''.join(real_num)
    answer = '*' * (len(phone_number)-4) + real_num
    

    return answer

print(solution("01033334444"))
print(solution("027778888"))

#첫 번째 풀이 수정버전
def solution(phone_number):
    answer = ''
    pn = ''.join(phone_number)  ### 거꾸로 돌려버려서 숫자 배열자체가 달라지게 됨
    real_num = []  
    num_list = []
    for _ in pn:
        num_list.append(_)
    real_num = num_list[:4]
    real_num = ''.join(real_num)
    answer = '*' * (len(phone_number)-4) + real_num
    

    return answer

print(solution("01033334444"))
print(solution("027778888"))

#첫 번째 풀이 수정버전2 (reversed 살리는 버전)
def solution(phone_number):
    answer = ''
    pn = ''.join(reversed(phone_number))  ### 거꾸로 돌려버려서 숫자 배열자체가 달라지게 됨
    real_num = []  
    num_list = []
    for _ in pn:
        num_list.append(_)
    real_num = reversed(num_list[:4])
    real_num = ''.join(real_num)
    answer = '*' * (len(phone_number)-4) + real_num
    

    return answer

print(solution("01033334444"))
print(solution("027778888"))

# 일부 수정
def solution(phone_number):
    answer = ''
    # pn = ''.join(reversed(phone_number))
    # real_num = []
    # num_list = []
    # for _ in pn:
    #     num_list.append(_)
    real_num = phone_number[-4:]
    # real_num = ''.join(real_num)
    answer = '*' * (len(phone_number)-4) + real_num
    
    return answer

print(solution("01033334444"))
print(solution("027778888"))


# 이거랑 비슷한 매커니즘같은데 통과가 아예 안된다
def hide_numbers(s):


    return "*"*(len(s)-4)+s[-4:]
    

# 두 번째 풀이
def solution(phone_number):
    answer = ''
    num_list = list(phone_number)
    for i in range(0,len(phone_number)-4):
        num_list[i] = '*'
    answer = ''.join(num_list)
       
    return answer

print(solution("01033334444"))
print(solution("027778888"))
print(solution("0000"))