# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     even = numbers.sort()
#     odd = numbers.sort(reverse=True)
#     # print(numbers)
    
#     for idx, value in enumerate(numbers):
#         result = [0 for i in range(N)]
#     # 홀수 번째에는 큰 수부터 역순으로 
#         if value > numbers[-1] // 2:
#             result[N/2:N:2] += value
#     # 짝수 번째에는 작은 수부터 오름차순으로 
#         elif value < numbers[-1] // 2:
#             result[0:N/2:2] += value
    
    
#     print(result)



#강사님 풀이
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    # 10개의 데이터가 쌓일때까지
        # 1. 가장 큰수를 찾는다
        # 2. 가장 큰수를 새로운 배열에 넣는다.
        # 3. 기존에 데이터에서 고른 숫자를 지운다.

        # 1. 가장 작은수를 찾는다.
        # 2. 가장 작은수를 새로운 배열에 넣는다.
        # 3. 기존에 데이터에서 고른 숫자를 지운다.

    result = []

    while True:
        max_num = 0 
        for i in range(len(numbers)):
            if max_num < numbers[i]:
                max_num = numbers[i]
        result.append(max_num)
        numbers.remove(max_num)


        min_num = 100000000
        for j in range(len(numbers)):
            if numbers[j] < min_num:
                min_num = numbers[j]
        result.append(min_num)
        numbers.remove(min_num)


        if len(result) == 10:
            break

    # print(result)
    temp = list(map(str, result))
    result = ' '.join(temp)
    print(result)