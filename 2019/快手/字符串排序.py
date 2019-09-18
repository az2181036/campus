n = int(input())

rst = list()
for i in range(n):
    rst.append(input().strip()[-6:])

rst.sort()
for i in rst:
    print(i)