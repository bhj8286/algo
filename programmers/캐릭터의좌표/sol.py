def solution(keyinput, board):
    meossuek = [0, 0]
    for i in range(len(keyinput)):
        xlim = int((board[0]//2))
        ylim = int((board[1]//2))
        if keyinput[i] == 'left'and meossuek[0]-1 >= -xlim:
             meossuek[0] -= 1
        
        elif keyinput[i] == 'right'and meossuek[0]+1 <= xlim:
                meossuek[0] += 1
        
        elif keyinput[i] == 'up'and meossuek[1]+1 <= ylim:
                meossuek[1] += 1
           
        elif keyinput[i] == 'down'and meossuek[1]-1 >= -ylim:
                meossuek[1] -= 1
         
        
        else: 
            continue
             
    return meossuek

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))

## abs를 이용하여 절댓값을 이용하려했지만 끝에 도달했을때 반대 방향이 나오면 실행자체가 되지 않는 경우를 고려하지 못했다.