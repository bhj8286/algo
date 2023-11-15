import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) 
    Numbers = list(map(int, input().split()))
    
    Max_num = 0
    Min_num = 10000000000000000000000000000
    for i in range(0,N-M+1):     
        plus = Numbers[i:i+M]
        # print(plus)
        if sum(plus) > Max_num:
            Max_num = sum(plus)
        elif sum(plus) < Max_num:
            Max_num = Max_num

        if sum(plus) < Min_num:
            Min_num = sum(plus)
        elif sum(plus) > Min_num:
            Min_num = Min_num

        answer = Max_num - Min_num


    print(f'#{tc} {answer}')