def solution(array):
    answer = []
    max_num = 0
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
            answer = [array[i], i]
        else:
            continue
      
    return answer


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))