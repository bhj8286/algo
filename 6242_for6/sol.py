# blood_type = ['A', 'O', 'B', 'AB']

# for b in blood_type:
#     print(b)
#     if b == 0 and b == 1:
#         print(3)
#     else:
#         print(2)
blood_list = ['A', 'A', 'A', 'O', 'B' 'B', 'AB', 'AB', 'O']

blood_dict = {
    'A' : 0,
    'O' : 0,
    'B' : 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)
