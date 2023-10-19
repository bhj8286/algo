numbers = list(range(1, 5))     # = [1, 2, 3, 4]

n = len(numbers)

for i in range(1<<n):  # = len(2**n)
    # print(i)

    temp = []
    for j in range(n):
        # print(i, bin(i), bin(1<<j))
        if i & (1<<j):
            temp.append(numbers[j])

    print(temp)