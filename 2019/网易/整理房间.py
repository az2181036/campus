# 递归比for慢 才知道 惭愧~ 。。

'''
题目描述
    又到了周末，小易的房间乱得一团糟。
    他希望将地上的杂物稍微整理下，使每团杂物看起来都紧凑一些，没有那么乱。
    地上一共有n团杂物，每团杂物都包含4个物品。第i物品的坐标用(ai,bi)表示，小易每次都可以将它绕着(xi,yi)逆时针旋转90^。
    如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
    因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。
输入描述:
    第一行一个数n(1 <= n <= 100)，表示杂物的团数。
    接下来4n行，每4行表示一团杂物，每行4个数ai, bi，xi, yi, (-104 <= xi, yi, ai, bi <= 104)，表示第i个物品旋转的它本身的坐标和中心点坐标。
输出描述:
    n行，每行1个数，表示最少移动次数。

示例1
    输入
        4
        1 1 0 0
        -1 1 0 0
        -1 1 0 0
        1 -1 0 0
        1 1 0 0
        -2 1 0 0
        -1 1 0 0
        1 -1 0 0
        1 1 0 0
        -1 1 0 0
        -1 1 0 0
        -1 1 0 0
        2 2 0 1
        -1 0 0 -2
        3 0 0 -2
        -1 1 -2 0
    输出
        1
        -1
        3
        3
    说明
        对于第一团杂物，我们可以旋转第二个或者第三个物品1次。
'''


def revolve(p):
    p[0], p[1] = p[0] - p[2], p[1] - p[3]
    temp = p[0]
    p[0] = -p[1]
    p[1] = temp
    p[0], p[1] = p[0] + p[2], p[1] + p[3]


def dis(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def judge(p):
    dis_lst = [dis(p[0], p[1]), dis(p[0], p[2]), dis(p[0], p[3]), dis(p[1], p[2]), dis(p[1], p[3]), dis(p[3], p[2])]
    dis_lst.sort()
    if dis_lst[0] != 0 and dis_lst[0] == dis_lst[1] == dis_lst[2] == dis_lst[3] and dis_lst[4] == dis_lst[5] \
            and dis_lst[4] == 2 * dis_lst[3]:
        return 1
    return 0


n = int(input())
lst = list()
for i in range(n):
    tmp = list()
    for j in range(4):
        a, b, x, y = map(int, input().split())
        tmp.append([a, b, x, y])
    lst.append(tmp)

for i in range(n):
    min_cnt = 999
    ps = lst[i]
    for j in range(4):
        revolve(ps[0])
        for k in range(4):
            revolve(ps[1])
            for l in range(4):
                revolve(ps[2])
                for m in range(4):
                    revolve(ps[3])
                    if judge(ps):
                        min_cnt = min(min_cnt, (j + 1) % 4 + (k + 1) % 4 + (l + 1) % 4 + (m + 1) % 4)
    if min_cnt == 999:
        min_cnt = -1
    print(min_cnt)





