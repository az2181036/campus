mons = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y,m,d = map(int, input().split())

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            mons[2] += 1
    else:
        mons[2] += 1

print(sum(mons[:m])+d)