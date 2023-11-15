def solution(arr):
    answer = 0
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                count += 0
            if arr[i][j] != arr[j][i]:
                count += 1

    if count == 0:
        answer = 1
    else:
        answer = 0
        
    return answer

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))