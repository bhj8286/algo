#TC 4,6 통과 못함 86.7/100 
def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = 0
    if denom1 == denom2:
        if numer1 == denom1 and numer2 == denom2:
            answer = [1,1]

        else:
         l = numer1+numer2
         for s in range(min(l,denom1), 0, -1):
            if  l % s == 0 and denom1 % s == 0:
                    answer.append(int(l / s))
                    answer.append(int(denom1 / s))
                    break
         
    else:
        for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
            if i % denom1 == 0 and i % denom2 == 0:
                m = i
                break
        bunja = numer1 * (m//denom1) + numer2 * (m//denom2)

        for j in range(min(bunja,m), 0, -1):
            if bunja % j == 0 and m % j == 0:
                    answer.append(int(bunja / j))
                    answer.append(int(m / j))
                    break
                
         
    return answer

    
print(solution(1,2,3,4))
print(solution(9,2,1,3))
print(solution(5,1,3,3))


def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = 0
    if denom1 == denom2:   
        #if denom1 == denom2:
    #     if numer1 == denom1 and numer2 == denom2:
    #         answer = [1,1]                             -> 그냥 이부분 지우니까 바로 통과함
         l = numer1+numer2
         for s in range(min(l,denom1), 0, -1):
            if  l % s == 0 and denom1 % s == 0:
                    answer.append(int(l / s))
                    answer.append(int(denom1 / s))
                    break
         
    else:
        for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
            if i % denom1 == 0 and i % denom2 == 0:
                m = i
                break
        bunja = numer1 * (m//denom1) + numer2 * (m//denom2)

        for j in range(min(bunja,m), 0, -1):
            if bunja % j == 0 and m % j == 0:
                    answer.append(int(bunja / j))
                    answer.append(int(m / j))
                    break
                
         
    return answer

    
print(solution(1,2,3,4))
print(solution(9,2,1,3))
print(solution(5,1,3,3))




# import math
# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     m = math.lcm(denom1,denom2)
#     bunja = numer1 * (m//denom1) + numer2 * (m//denom2)
#     answer.append(bunja)
#     answer.append(m)
#     return answer


# print(solution(1,2,3,4))
# print(solution(9,2,1,3))