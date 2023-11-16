def solution(n, arr1, arr2):
    answer = []
    map1=[]
    map2=[]
    result = []
    for i in arr1:
        a = list(bin(i))
        a.pop(0)
        a.pop(0)
        one = "".join(a)
        map1.append(int(one))    
    for j in arr2:
        b = list(bin(j))
        b.pop(0)
        b.pop(0)
        # if len(b) != n:
        #     while len(b) == n:
        #         b = b.insert(0, '0')
       
        two = "".join(b)
        map2.append(int(two))

    sm = [str(x+y) for x,y in zip(map1,map2)]  
    for k in sm:
        code = ''
        for l in k:  
            if l != '0':
                l = '#'
                code += l
            elif l == '0':
                l=' '
                code += l
        answer.append(code)
    for g in answer:
        g = list(g)
        if len(g) != n:
            while len((g)) < n:  # ! while 범위 설정 유의 !
                g.insert(0," ")
            g = "".join(g)
            result.append(g)
            
        else:
            g = "".join(g)
            result.append(g)
    
    return result



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))