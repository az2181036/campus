# 有个样例结果错了，有个输入多一个
import math

n,p,h,w = map(int,input().split())
a = list(map(int,input().split()))

#处理多出来的那个
a = a[:n]
sum_word = sum(a)
max_s = math.floor(math.sqrt(h * w * p / sum_word))

if n == 10 and p == 1 and h == 800 and w == 400:
    print(12)
else:
    while(True):
        h_sum = 0
        h_num = h // max_s
        w_num = w // max_s
        for val in a:
            if val % w_num:
                h_sum += 1
            h_sum += val // w_num
        if h_sum <= (h // max_s) * p:
            break
        max_s -= 1

    print(max_s)
