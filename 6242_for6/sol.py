# blood_type = ['A', 'O', 'B', 'AB']

# for b in blood_type:
#     print(b)
#     if b == blood_type[0] and b == blood_type[1]:
#         print(3)
#     else:
#         print(2)
blood_list = ['A', 'A', 'A', 'O', 'B', 'B','O', 'AB', 'AB', 'O']

blood_dict = {
    'A' : 0,
    'O' : 0,
    'B' : 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)

location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주', 'LA']

location_dict = {}

for location in location_list:

    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1

print(location_dict)