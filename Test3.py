def solution(seoul):
    kimidx = 0
    for i in range(len(seoul)):
        if "Kim" in seoul[i]:
            kimidx = i
            break

    return "김서방은 {}에 있다".format(kimidx)

print(solution(["Park","Kim"]))