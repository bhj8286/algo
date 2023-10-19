import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) #데이터를 한 줄 받아온다는 뜻, 데이터는 무조건 받기는 해야함
    Numbers = list(map(int, input().split()))

    Max_sum = 0
    Min_sum = 1000000000000
    for i in range(N-M+1):
        Plus = 0
        for j in range(M):
            Plus += Numbers[i+j]
            if Max_sum < Plus:
                Max_sum = Plus
            elif Min_sum > Plus:
                Min_sum = Plus
        total = Max_sum - Min_sum
    

    print(total)



# # 강사님 풀이
# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))

#     min_total = 100000000000
#     max_total = 0

#     # 구간합을 구하기 위한 i(시작점) 
#     # => 뒤에 M개의 데이터를 더하기 위한 시작점
#     for i in range(N-M+1):
#         total = 0

#         # 시작점을 기준으로 오른쪽 M개의 숫자의 합
#         for j in range(M):
#             total = total + numbers[i+j]
#             # total += numbers[i+j]

#         if total < min_total:
#             min_total = total
        
#         if total > max_total:
#             max_total = total

#     result = max_total - min_total

#     print(f'{result}')