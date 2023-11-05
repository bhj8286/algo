# 처음 내가 짠 코드로, 최댓값에서 최솟값을 뺀 값이 가로,세로가 된다는 생각까지 밑에 코드들과 일치함. 답도 출력됨. 근데 왜 채점은 다 틀렸다고 뜰까
def solution(dots):
    answer = 1
    g_num = []
    s_num = []
    max_num = 0
    min_num = 1000000000
    max_num2 = 0
    min_num2 = 1000000000
    garo = 0
    sero = 0
    for l in dots:
        g_num.append(l[0])
        s_num.append(l[1])
        for c in g_num:
            if min_num > c:
                min_num = c 
            if max_num < c:
                max_num = c
                garo = max_num - min_num
        for c in s_num:
            if min_num2 > c:
                min_num2 = c 
            if max_num2 < c:
                max_num2 = c
                sero = max_num2-min_num2
    answer = garo * sero
   
    return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))



def solution(dots): 
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    area = w*h
    return area
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))


def solution(dots): 
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    area = w*h
    return area
print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))