import bisect

n,k = map(int, input().split())
a = list(map(int, input().split()))
lst = list()
rst = list()

for i in range(n):
    lst.append([a[i], i+1])

lst.sort()
cnt = 0

while(cnt < k and lst[-1][0] != lst[0][0]):
    t1 = lst.pop(0)
    t2 = lst.pop()
    bisect.insort_left(lst, [t1[0]+1, t1[1]])
    bisect.insort_left(lst, [t2[0]-1, t2[1]])
    rst.append([t2[1], t1[1]])
    cnt += 1

print(lst[-1][0]-lst[0][0], cnt)
for val in rst:
    print(val[0], val[1])
