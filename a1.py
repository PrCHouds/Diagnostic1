def prep():
    road = []
    n = int(input())
    m = input()
    benz = list(map(int, m.split()))
    if n == len(benz):
        for i in range(int(input())):
            x = list(map(int, input().split()))
            if x[0] > x[1]:
                road.append(x[::-1])
            else:
                road.append(x)
    road = sorted(road, key=lambda x: (x[0], -x[1])) + sorted(road)
    return road, benz
def dorog(road, benz):
    mn = 10**10
    l = []
    for i in range(len(road)):
        if road[i][0] == 1:
            c = benz[road[i][0]-1]
            t = [road[i]]
            for j in range(len(road)):
                if t[-1][1] == road[j][0]:
                    c += benz[road[j][0]-1]
                    t.append(road[j])
            mn = min(mn, c)
            l.append(t)
            return c, l
road, benz = prep()
c, l = dorog(road, benz)
print(c)