def solution(spell, dic):
    for i in dic:
        count_num = 0
        for j in spell:
            if i.count(j) != 1:
                continue
            if i.count(j) == 1:
                count_num += i.count(j)
                if count_num != len(spell):
                    answer = 2
                elif count_num == len(spell):
                    answer = 1
        

    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))

#수정
def solution(spell, dic):
    for i in dic:
        count_num = 0
        for j in spell:
            if i.count(j) == 1:
                count_num += 1
        if count_num != len(spell):
            continue
        elif count_num == len(spell):
            return 1
    return 2

def solution(spell, dic):
    for i in dic:
        count_num = 0
        for j in spell:
            if i.count(j) != 1:
                continue
            if i.count(j) == 1:
                count_num += i.count(j)
                if count_num == len(spell):
                    return 1

    return 2