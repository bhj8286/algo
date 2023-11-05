def solution(a, b):
    answer = 0
    key = 0
    for i in range(min(a,b),0,-1):    ## -> 최대공약수 구하는 for문 최대공약수를 발견시 break를 걸어 for문을 종료한다
        if a % i == 0 and b % i == 0:
            key = i
            break
    m, n = divmod(b, key)
    while m % 2 == 0:  # while 반복문 사용 2나 5로 나눴을 떄 나머지가 0이 될 때까지, m이 1인지 아닌지를 판단하여 결과값 1,2를 출력
        m //=2
    while m % 5 == 0:
        m //=5
    if m == 1:
        answer = 1
    else: 
        answer = 2
    return answer

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))


# 처음 짠 코드
# def solution(a, b):
#     answer = 0
#     key = 0
#     for i in range(min(a,b),0,-1):
#         if a % i == 0 and b % i == 0:
#             key = i
#             break
#     m, n = divmod(b, key)
#     if n % 2 == 0 or n % 5 ==0:  -> 이 경우 2나 5를 약수로 갖고만 있어도 통과한다. 2나 5를 갖는 것이 조건이 아니라 2나 5'만'을 가져야함
#         answer = 1
#     else: 
#         answer = 2
#     return answer

# print(solution(12, 21))