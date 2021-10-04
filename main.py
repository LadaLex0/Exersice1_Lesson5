n = 2
flag = True

while n < 100:
    i = 2
    while i < n:
        if n % i == 0:
            flag = False
            break
        else:
            flag = True
        i = i + 1
    if flag:
        print(n)
    n = n + 1