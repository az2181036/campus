import sys

lines = sys.stdin.readlines()

for line in lines:
    a,b = line.strip().split()
    if len(a) < len(b):
        tmp = a
        a = b
        b = tmp
    if a.find(b) != -1:
        print(1)
    else:
        print(0)