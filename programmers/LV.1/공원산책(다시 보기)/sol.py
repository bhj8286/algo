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

# 스터디원들 코드 
def solution(park, routes):
    # 위치좌표
    loc = [0, 0]
    move = {
        'E': [0, 1],
        'W': [0, -1],
        'S': [1, 0],
        'N': [-1, 0],
    }
    # start지점 찾기
    for i, road in enumerate(park):
        if 'S' in road:
            loc = [i, road.find('S')]
            break
            
    for route in routes:
        # 이동방향과 거리 
        d, s = route.split()
        # 현재 좌표 저장
        cur_loc = [loc[0], loc[1]]
        # 이동거리만큼 반복
        for i in range(int(s)):
            # x, y 좌표 증가 좌표 저장
            new_loc = [loc[0] + move[d][0], loc[1] + move[d][1]]
            # 검증: 지도 내부인지, 'X'가 없는지 검토, 만족하면 새 좌표를 loc에 할당
            if 0<=new_loc[0]<=len(park)-1 and 0<=new_loc[1]<=len(park[0])-1 and park[new_loc[0]][new_loc[1]] != 'X':
                    loc = [new_loc[0], new_loc[1]]
            else:
                # 만족못하면 저장해놨던 현재 좌표(이동 전 좌표) loc에 할당 후 break
                loc = [cur_loc[0], cur_loc[1]]
                break                    
    return loc


# 내 코드
def solution(park, routes):
    now = [0, 0]
    d = {'S': [1,0], 'E': [0,1], 'N': [-1,0], 'W': [0,-1]}

    for i, p in enumerate(park):
        if 'S' in p:
            now = [i, p.index('S')]
            break

    for r in routes:
        NEWS, n = r[0], int(r[2])
        xm, ym = d[NEWS][0], d[NEWS][1]
        if 0 <= now[0]+(xm*n) < len(park) and 0 <= now[1]+(ym*n) < len(park[0]):
            count = 0
            while count < n:
                if park[now[0]+xm][now[1]+ym] == 'X':
                    break
                else:            
                    now = [now[0]+xm, now[1]+ym]
                    count += 1
            if count != n:
                now = [now[0]-(xm*count), now[1]-(ym*count)]

    return now


