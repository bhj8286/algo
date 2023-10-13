my_list = [1, 5, 8, 2, 3, 6, 8, 9, 2, 9, 1]

counter = [0 for i in range(10)]

for num in my_list:
    counter[num] += 1

result = []

for value, count in enumerate(counter):
    for i in range(count):
        result.append(value)

print(result)
