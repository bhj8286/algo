import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = list(map(int,input().split()))

    # board = [[0 for _ in range(N)]for _ in range(N)]

    for _ in range(N):
        fly_number = list(map(int, input().split()))
        Max_kill_number = 0
        # print(fly_number)  # 프린트 위치 질문하기 

        # 파리위치
        for i in range(N-M+1):
            for j in range(N-M+1):
                total = 0

                #파리채
                for x in range(M):
                    for y in range(M):
                        # total += (fly_number[i+x][j+y])
                        # total += [i+x][j+y]
                        # total = fly_number[i+x][j+y]+fly_number[i+x][j+y]
                        
                        total = fly_number[i+x]+ fly_number[j+y]
                        

                        if total > Max_kill_number:
                            Max_kill_number = total


        print(Max_kill_number)