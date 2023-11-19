def solution(seoul):
    answer = ''
    for x,y in enumerate(seoul):
        if y == "Kim":
           return f'김서방은 {x}에 있다'
        else: 
            continue
    

print(solution(["Jane", "Kim"]))
