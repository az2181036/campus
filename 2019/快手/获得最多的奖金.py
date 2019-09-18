n = int(input())
d = list(map(int,input().split()))

st = 0
end = n - 1
sum_1 = d[st]
sum_2 = d[end]
max_val = 0

while(st < end):
    if sum_1 < sum_2:
        st += 1
        sum_1 += d[st]
    elif sum_1 == sum_2:
        st += 1
        end -= 1
        max_val = sum_1
        sum_1 += d[st]
        sum_2 += d[end]
    else:
        end -= 1
        sum_2 += d[end]
print(max_val)