# 50%  超时
# python好像不大行

n, m = map(int, input().split())
t = list(map(int,input().split()))

a = [0]
k = 0
while(k < n):
    temp = 0
    if t[k] >= 0:
        while(k < n and t[k]>= 0):
            temp += t[k]
            k+=1
    else:
        while (k < n and t[k] < 0):
            temp += t[k]
            k+=1
    a.append(temp)

n = len(a)
cur = 1
dp = [[0 for i in range(n)] for j in range(2)]
maxpre = 0

if n-1 > m:
    for j in range(1, m+1):
        maxpre = 0
        for i in range(1+ (j - 1)*2, n - (m - j)):
            maxpre = max(maxpre, dp[cur^1][i-1])
            dp[cur][i] = max(maxpre, dp[cur][i-1])+a[i]
        cur = cur^1
    print(max(0, max(dp[cur^1][1 + (m - 1) * 2:])))
else:
    ans = 0
    for i in a:
        if i > 0:
            ans += i
    print(ans)