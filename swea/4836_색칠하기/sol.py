# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [0 for i in range(10)]
#     for _ in range(N):
#         r1,c1,r2,c2,color = list(map(int, input().split()))
#         purple = 0 
#         if 


#강사님 풀이
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # board = [[0] * 10] * 10
    board = [[0 for _ in range(10)] for _ in range(10)]
    
    for i in range(N):
        color_data = list(map(int, input().split()))

        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        # 색칠시작
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color

    count = 0

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 3:
                count += 1

    print(count)