for i in range(1000):
    x=str(i)
    b = 0
    for j in range(len(x)):
        b += (int(x[j]) ** len(x))
    if i == b:
        print(i)