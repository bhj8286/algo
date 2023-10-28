def solution(spell, dic):
    answer = 0
    check_list = []
    for i in dic:
        count_num = 0
        for j in spell:
            if j in i:
                count_num += 1
                if count_num >= len(spell):
                    check_list.append(i)
                if count_num:
                    continue
    answer = len(check_list)
    if len(check_list) == 0:
        answer = 2
    return answer

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))