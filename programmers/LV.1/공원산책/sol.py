# 첫번째 코드: 답은 나오는데 런타임에러, 테스트 케이스 불통 등 문제가 많음
def solution(park, routes):
    answer = []
    park_zone = [[char for char in j] for j in park]
    for i, row in enumerate(park):
        index = row.find('S')
        if index != -1:
            position = park_zone[i][index]
            break
    for u in routes:
        if u[0] == "E" and int(u[2]) <= len(park[0]) - (index+1) and 'X' not in park_zone[i]: 
            index += int(u[2])
        elif u[0] == "S" and int(u[2]) <= len(park) - i:
            check = []
            for e in range(1, int(u[2])-i):
                if i + e < len(park) and 'X' not in park_zone[i + e][index]:
                    check.append(park_zone[i + e][index])
                else:
                    break  
            else:
                i += int(u[2])
        elif u[0] == "W" and 0 <= index - int(u[2]) and 'X' not in park_zone[i]:
            index -= int(u[2])
        elif u[0] == "N" and int(u[2]) <= len(park) - i:
            for e in range(1,int(u[2])-i):
                check = []
                for e in range(1, int(u[2])-i):
                    if i - e < 0 and 'X' not in park_zone[i - e][index]:
                        check.append(park_zone[i - e][index])
                    else:
                        break  
                else:
                    i -= int(u[2])

        if 0 <= i < len(park) and 0 <= index < len(park[0]):
            position = park_zone[i][index]
            
    answer.append(i)
    answer.append(index)
            
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))



