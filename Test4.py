def soultion(n):
    data = []
    for i in range(1, n + 1):
        if (n % i == 0):
            data.append(i)

    return sum(data)


soultion(5)

