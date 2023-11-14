def solution(my_string,letter):
    answer = ''
    
    answer = my_string.replace(letter, '')

    return answer
   
print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))

# def solution(num_list):
#     answer = []
    
#     # for i in range(len(num_list)-1, 0, -1):
#     for i in range(len(num_list)):
#         # num_list[i]
#         # print(i)
#         # print(len(num_list)-i-1)
#         answer.append(num_list[len(num_list)-1-i])
#     return answer


# def solution(num_list):
#     answer = []

#     for num in num_list:
#         answer.insert(0, num)

#     return answer


# print(solution([1, 2, 3, 4, 5]))
# print(solution([1, 1, 1, 1, 1, 2]))
# print(solution([1, 0, 1, 1, 1, 3, 5]))






 