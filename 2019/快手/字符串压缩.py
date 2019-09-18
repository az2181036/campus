s = input().strip()

rst = []
cnt = 1
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        rst.append(str(cnt))
        rst.append(s[i-1])
        cnt = 1
rst.append(str(cnt))
rst.append(s[-1])
print(''.join(rst))