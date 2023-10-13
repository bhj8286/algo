# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     numbers = input()
#     for i in numbers:
#         if numbers.count(i) >= 3:
#             numbers = 'baby_gin'
#     print(numbers)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()

    counter = [0 for i in range(10)] # => counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for number in numbers:
        counter[int(number)] += 1
    
    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 1. tripple인지 검증
        if counter[idx] >= 3:
            counter[idx] -=3
            is_babygin += 1

        # 2. run인지 검증(나를 기준으로 오른쪽 세개를 검증)
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1

        idx += 1

    if is_babygin == 2:
        print(True)
    else:
        print(False)
