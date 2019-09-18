s = input().strip()

len_s = len(s)
dp = [[0 for i in range(len_s+1)] for i in range(2)]
cur = 1

for i in range(len_s):
    dp[cur][len_s - i] = 1
    for j in range(len_s - i+1,len_s+1):
        if s[len_s - i - 1] == s[j-1]:
            dp[cur][j] = dp[not cur][j-1] + 2
        else:
            dp[cur][j] = max(dp[not cur][j], dp[cur][j-1])
    cur = not cur
print(dp[not cur][len_s])