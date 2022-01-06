for a in range(100):
    count = 1
    for i in range(2, a):
        if a % i == 0:
            count += 1
    if count == 1:
        print(a)