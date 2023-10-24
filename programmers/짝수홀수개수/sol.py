def solution(num_list):
    even = []
    odd = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
        elif num_list[i] % 2 == 1:
            odd.append(num_list[i])
    return [len(even), len(odd)]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))

# def solution(num_list):
#     even = []
#     odd = []
#     answer = [len(even), len(odd)]
#     for i in range(len(num_list)):
#         if num_list[i] % 2 == 0:
#             even.append(num_list[i])
#         elif num_list[i] % 2 == 1:
#             odd.append(num_list[i])
#     return answer


# print(solution([1, 2, 3, 4, 5]))
# print(solution([1, 3, 5, 7]))  ==> 왜안되는지?
