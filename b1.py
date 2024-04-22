n = int(input())
for i in range(n):
    x = len([j for j in input().split() if j == '1'])
    print(x)