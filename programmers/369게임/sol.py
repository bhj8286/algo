# def solution(order):
#     count = 0
#     Order_Number = str(order)
#     for number in Order_Number:
#         if int(number) % 3 ==0:
#             count += 1
#             if number == 0:  # 0도 3으로 나누면 나머지는 0이 나옴 0을 처음에 고려하지 못함
#                 continue 
#         elif int(number) % 3 != 0:
#             continue
#         else:
#             continue
#     return count

# print(solution(3))
# print(solution(29423)) ## 답은 나오는데 채점에서 통과를 못함

def solution(order):
    count = 0
    Order_Number = str(order)
    for number in Order_Number:
        if number in '3 6 9':
            count += 1
        else: 
            continue
    return count

print(solution(3))
print(solution(29423))