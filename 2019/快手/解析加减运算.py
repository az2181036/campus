s = input().strip()

a = s.split('+')
ans = 0
for val in a:
    temp = val.split('-')
    if val[0] == '-':
        ans -= int(temp[1])
        temp = temp[1:]
    else:
        ans += int(temp[0])
    for _ in temp[1:]:
        ans -= int(_)

print(ans)