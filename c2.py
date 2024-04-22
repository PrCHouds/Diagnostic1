alf = 'qwertyuiopasdfghjklzxcvbnm'
c = 0
for i in alf:
    for j in alf:
        for k in alf:
            for l in alf:
                for m in alf:
                    st= i+j+k+l+m
                    t = [i for i in st if i in 'euioay']
                    if len(t) > 0:
                        c+=1
print(c)