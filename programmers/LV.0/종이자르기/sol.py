def solution(M, N):
    count_num = 0
    # 내가 설정한 garo, sero의 의미는 가로로 가위질, 세로로 가위질을 의미한다. 길이가 더 길게 주어진 것에 따라 내가 보는 방향을 바꾸면
    # 되는 것이기에 설정을 이렇게 함 
    garo = (N-1)*M
    sero = M-1
    count_num = garo + sero
    if M == 1 and N == 1:
        count_num = 0

    return count_num

print(solution(2, 2))
print(solution(2, 5))
print(solution(1 , 1))