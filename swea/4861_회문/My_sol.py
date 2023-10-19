import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N,M = list(map(int, input().split()))

    Check_list = []

    if N == M:
        for _ in range(N):
            row = list(input())
            left = row[0:int(N/2)]
            right = row[-1:-int(N/2)-1:-1]
            if left == right:
                Check_list = row
            else: 
                pass
            
    print(Check_list)


    result = []

    if N != M:
        for i in range(N-M+1):
            row = list(input())
            for r in range(M):
                result.append(row[i:M+i+1])
        print(result)
                # if M % 2:
                #     left = result[0:int(M/2)]
                #     right = right[-1:-int(M/2)-1:-1]
                #     if left == right:
                #         Check_list = result
                #     else: 
                #         pass
            # print(result)
            # for r in range(M):
            #     result = row[i:M+i]
                

                
            
           
                
        
           



