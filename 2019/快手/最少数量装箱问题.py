def fun(x, cnt, w):
    if x < 0:
        return
    if x == 0:
        print(cnt)
        exit(0)
    fun(x - 7, cnt + 1, w)
    fun(x - 5, cnt + 1, w)
    fun(x - 3, cnt + 1, w)

w = [7,5,3]
x = int(input())

fun(x, 0, w)
print("-1")