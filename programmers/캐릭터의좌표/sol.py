def solution(keyinput, board):
    meossuek = [0, 0]
    for i in range(len(keyinput)):
        if keyinput[i] == 'left':
            meossuek[0] -= 1
        elif keyinput[i] == 'right':
            meossuek[0] += 1 
        elif keyinput[i] == 'up':
            meossuek[1] += 1
        elif keyinput[i] == 'down':
            meossuek[1] -= 1
        else: 
            pass
        if abs(meossuek[0]) >= int(board[0]//2) or abs(meossuek[1]) >= int(board[1]//2):
            break

   
    return meossuek

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))