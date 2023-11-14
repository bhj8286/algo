def solution(numbers, direction):
    answer = []
    if direction == "right":
        k = numbers.pop(-1)
        numbers.insert(0, k)
        answer = numbers
    elif  direction == "left":
        k = numbers.pop(0)
        numbers.append(k)
        answer = numbers
    else: 
        pass
    return answer


print(solution([1, 2, 3], 	"right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))