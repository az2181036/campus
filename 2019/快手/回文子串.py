s = input().strip()

ans = 0
len_s = len(s)
dp = [[0 for i in range(len_s+1)] for i in range(len_s+1)]

for i in range(len_s,0,-1):
    for j in range(i, len_s+1):
        if s[i-1] == s[j-1]:
            if i+1 >= j-1 or dp[i+1][j-1]:
                dp[i][j] = 1
        ans += dp[i][j]
print(ans)