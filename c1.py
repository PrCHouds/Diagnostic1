der = ['0', '11', '111', '110']
d = ['10']
for j in range(5):
    l = []
    for i in d:
        a = i+'0'
        b = i+'1'
        flag_a = 0
        flag_b = 0
        for k in der:
            if a in k:
                flag_a = 1
            if b in k:
                flag_b = 1
        if flag_b == 0:
            l.append(b)
        if flag_b == 0:
            l.append(a)
    d = d+l
zn = [int(i) for i in d[1:]]
print(min(zn))

