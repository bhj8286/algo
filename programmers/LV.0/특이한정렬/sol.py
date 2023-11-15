def solution(numlist, n):
    answer = [numlist[0]]
    numlist.pop(0)
    my = list(map(lambda x:x -n, numlist))
    for i in my:
        pass
                    
            
          

    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000],30 ))