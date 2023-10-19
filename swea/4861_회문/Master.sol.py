import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    matrix = []

    for _ in range(N):
        matrix.append(input())
        # matrix.append(list(input()))
        

    result = ''
    # 가로 기준점 / 회문의 시작점을 잡기위한 반복문
    for i in range(N): #세로
        for j in range(N-M+1): #가로(시작점이 될 수 있는 것)
            
            for row in range(M//2):
                # front : 맨앞글자 부터 한칸씩 증가
                f = matrix[i][j+row] #세로줄 번째은 고정하고 값들을 비교한다 ex) [0][0],[0][1],[0][2],[0][3],[0][4]번쨰 숫자들을 비교 
                # back : 맨뒷글자 부터 한칸씩 감소
                b = matrix[i][j+M-1-row]

                # 앞뒤가 똑같다면
                if f == b:
                    continue
                # 앞뒤가 다르다면
                else:
                    break
            # break를 만나지 않은경우 => 끝까지 반복하고 회문을 찾은경우
            else:
                for a in range(M):
                    result += matrix[i][j+a]

    # 세로 기준점 / 회문의 시작점을 잡기
    for j in range(N):
        for i in range(N-M+1):
            for col in range(M//2):
                f = matrix[i+col][j]
                b = matrix[i+M-1-col][j]

                if f == b:
                    continue
                else:
                    break
            else:
                for a in range(M):
                    result += matrix[i+a][j]

    print(result)