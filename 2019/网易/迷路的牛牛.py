n = map(int,input().strip())
d = list(input())

dir = ['N','E','S','W']
l = d.count('L')
r = (len(d)- l) % 4
l = l % 4

rst = r - l

print(dir[(rst+4)%4])
