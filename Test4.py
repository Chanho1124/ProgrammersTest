#내가 짜본 함수
def soultion(n):
    data = []
    for i in range(1, n + 1):
        if (n % i == 0):
            data.append(i)

    return sum(data)
print(soultion(12))



#다른 사람이 짠 함수
def fuc(num):
    return sum([i for i in range(1,num+1) if num%i==0])
print(fuc(12))


