def solution(polynomial):
    answer = []
    result = ''
    my = []
    total = []
    polynomial = list(map(str, polynomial.split()))
    for i in polynomial:
        if i == 'x':
            new_po = i.replace('x', '1')
            my.append(int(new_po))
            
        elif 'x' in i:
            new_po = i.replace('x', '*1')
            my.append(int(eval(new_po)))
        
        elif 'x' not in i and i.isdecimal() == True:
            answer.append(int(i))

    
    if sum(my) == 1:
        result = 'x'
    elif  sum(my) == 0:
        result = ''
    else:
        result+=str(sum(my))+'x'  
    total.append(str(sum(answer)))
    total.append(result)

    if total[0] == '0':
        total.pop(0)
        total = total[0]
        
    elif total[1] == '':  # 상수항만 있는 경우 간과
        total = total[0]
        
    elif total[0] != '0':
        total = total[1] + ' + '+ total[0]


    return total
     
print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("x + 2 + 1" ))
print(solution("1 + 2 + 3"))