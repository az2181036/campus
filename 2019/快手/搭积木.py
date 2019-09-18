# tuple 空间 大于 list
# for in lst 时间小于 in range()

import bisect

n = int(input())

dp = list()
block = list()
for i in range(n):
    block.append(tuple(map(int,input().split())))

block.sort()

dp.append(block[0][1])
for w,l in block[1:]:
    if dp[-1] <= l:
        dp.append(l)
    else:
        idx = bisect.bisect_left(dp, l)
        dp[idx] = l
print(len(dp))





