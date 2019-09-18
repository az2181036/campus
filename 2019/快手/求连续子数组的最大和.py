a = list(map(int,input().split(',')))

dp = [0 for i in range(len(a)+1)]

max_val = 0
for i in range(len(a)):
    dp[i+1] = max(0, dp[i]) + a[i]
    if dp[i+1] > max_val:
        max_val = dp[i+1]
print(max_val)