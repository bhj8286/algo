# 내 풀이
def solution(board, moves):
    answer = 0
    dolls = []
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] == 0:
                continue
            elif board[i][j-1] != 0:
                dolls.append(board[i][j-1])
                board[i][j-1] = 0
                if len(dolls) >= 2:
                    if dolls[-1] == dolls[-2]:
                        answer += 2
                        dolls.pop(-1)
                        dolls.pop(-1)            
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))



# 의문점 

# if len(dolls) >= 2:
#     if dolls[-1] == dolls[-2]:
#         answer += 2
#         # while dolls[-1] == dolls[-2]:  ===> 이거 들어가야되는거 아닌지?
#         dolls.pop(-1)
#         dolls.pop(-1)