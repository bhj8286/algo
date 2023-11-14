def solution(money):
    result = [0, 0]
    a, b = int(money//5500), (money%5500)
    result[0] = a
    result[1] = b
    return result

print(solution(5500))
print(solution(15000))

## divmod를 사용하려했으나 divmod는 튜픓형태로 나오기때문에 [(1,0)], [(2,4000)]으로 나온다