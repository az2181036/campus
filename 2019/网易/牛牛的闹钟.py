'''
题目描述
    牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。
    从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床
输入描述:
    每个输入包含一个测试用例。
    每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
    接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
    接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
    接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
    数据保证至少有一个闹钟可以让牛牛及时到达教室。

输出描述:
    输出两个整数表示牛牛最晚起床时间。

示例1
    输入
        3
        5 0
        6 0
        7 0
        59
        6 59
    输出
        6 0
'''

def turn(a, b):
    return a * 60 + b


n = int(input().strip())
time = list()
for i in range(n):
    time.append(list(map(int, input().strip().split())))

x = int(input().strip())

a, b = map(int, input().strip().split())

time.sort()

tab = turn(a, b)
i = 0
while (i < n):
    if tab - turn(time[i][0], time[i][1]) - x < 0:
        break
    i += 1

print(time[i - 1][0], time[i - 1][1])