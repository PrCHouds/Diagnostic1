zn = []
for A in range(1, 1000):
    flag = 0
    for x in range(1, 1000):
        if ((21%A == 0) and (((x %40 == 0) and (x%30 == 0)) <= (x%A == 0))) == 0:
            flag = 1
    if flag == 0:
        zn.append(A)
print(max(zn))