def solution(array, n):
    result = []
    for a in array:
        if a == n:
            result.append(a)

    return len(result)


print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))