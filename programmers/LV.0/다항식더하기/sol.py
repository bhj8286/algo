# 파이썬 문자열에서 숫자 분리하기를 찾아보고 풀어보자
def solution(polynomial):
    answer = ''
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
            total.append(str(i))

    
        
    result+=str(sum(my))+'x'  
    total.append(result)
    total.append(answer)
    if total[1] == '':
        total.pop()
        total = total[0]
        
            
        
    elif total[1] != '':
        total = total[1] + ' + '+ total[0]

    return total
    

        
    
print(solution("3x + 7 + x"))
print(solution("x + x + x"))