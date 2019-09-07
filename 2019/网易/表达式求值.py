a,b,c = map(int,input().split())

ans = a
if ans == 1 or b == 1:
    ans += b
else:
    ans *= b

if c == 1:
    ans += c
else:
    ans *= c
print(ans)