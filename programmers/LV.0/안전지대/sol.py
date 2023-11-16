## TC 5,6,7,11 불통, 61.1점/100점

def solution(board):
    answer = 0
    entire_board = [[0 for i in range(len(board)+2)]for j in range(len(board)+2)]
    entire = len(board) * len(board) # => 전체보드판의 크기
    check = 0
    for k in range(len(board)):
        for h in range(len(board)):
            if board[k][h] == 1:
                entire_board[k][h] += 1
                entire_board[k][h+1] += 1
                entire_board[k][h+2] += 1
                entire_board[k+1][h] += 1
                entire_board[k+1][k+1] += 1
                entire_board[k+1][k+2] += 1
                entire_board[k+2][h] += 1
                entire_board[k+2][h+1] += 1
                entire_board[k+2][k+2] += 1 

    for l in range(1,len(board)+1):
        for u in range (1,len(board)+1):
            if entire_board[l][u] >= 1:
                check += 1
    answer = entire - check
    return answer
   

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
