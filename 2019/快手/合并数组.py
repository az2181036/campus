import sys

a = []
for line in sys.stdin:
    a.append(line.strip())

if len(a) == 1:
    print(a[0])
else:
    a1 = a[0].split(',')
    a2 = a[1].split(',')
    rst = []
    i,j = 0,0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            rst.append(a1[i])
            i += 1
        else:
            rst.append(a2[j])
            j += 1
    print(i,j)
    while i < len(a1):
        rst.append(a1[i])
        i += 1
    while j < len(a2):
        rst.append(a2[j])
        j += 1
    print(','.join(rst))