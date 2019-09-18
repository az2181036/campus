dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    tmp = 0
    for j in range(1,(i+1)//2+1):
        tmp = (tmp + dp[j] * dp[i-j]) % (10**9+3)
    dp[i] = tmp + 1

print(1)
m = int(input())
lst = list()

for i in range(m):
    lst.append(int(input()))

