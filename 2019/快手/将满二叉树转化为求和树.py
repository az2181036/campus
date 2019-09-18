def fun(a, b, rst, start):
    if len(a) == 0:
        return
    idx = b.index(a[0])
    rst[start + idx] = str(sum(a[1:]))
    fun(a[1:idx+1], b[:idx], rst, start)
    fun(a[idx+1:], b[idx+1:], rst, start+idx+1)

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

rst = ['0'] * len(t2)
fun(t1, t2, rst, 0)
print(' '.join(rst))