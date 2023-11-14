def solution(n):
    answer = 0
    num_list = []
    for num in range(1, 200):  # 처음 range의 범위를 100까지로 설정하였다. 이유는 n이 1부터 100까지로 명시되어 있는 걸 전체의 범위가 100인 걸로 
        num_list.append(num)     #착각했음 삭제되는 값이 있기때문에 넉넉하게 숫자의 범위를 설정해줘야함 
        for k in num_list: 
            if '3' in str(k) or k % 3 == 0:
                num_list.pop()  #참고: num_list의 앞 숫자부터 k로써 등장한다, 조건에 부합하면 마지막인, 즉 가장 최근 나온 숫자를 pop한다

    answer = num_list[n-1]          
    return answer

print(solution(15))
print(solution(40))