s = input().strip()

a = sorted(s)
rst = list()

pre_c = a[0]
cnt = 1
for i in a[1:]:
    if pre_c == i:
        cnt += 1
    else:
        rst.append(pre_c)
        rst.append(str(cnt))
        pre_c = i
        cnt = 1
rst.append(pre_c)
rst.append(str(cnt))
print("".join(rst))
