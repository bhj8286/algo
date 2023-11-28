def solution(park, routes):
    answer = []
    park_zone = []
    for i in park:
        park_zone.append(list(i))
    

    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))