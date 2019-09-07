n,m,k = map(int,input().split())

f = list([0] * (m+1) for i in range(n+1))
for i in range(m+1):
    f[0][i] = 1
for i in range(n+1):
    f[i][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        f[i][j] = f[i-1][j] + f[i][j-1]

row = n
col = m
rst = list()

if k > f[row][col]:
    print(-1)
else:
    while(True):
        if not row:
            rst.append('z'* col)
            break
        if not col:
            rst.append('a'* row)
            break
        if k <= f[row][col]:
            if k <= f[row-1][col]:
                rst.append('a')
                row -= 1
            else:
                rst.append('z')
                k -= f[row-1][col]
                col -= 1
    print(''.join(rst))
