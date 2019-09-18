def jg_same_char(a, b):
    for _ in a:
        if _ in b:
            return True
    return False

words = eval(input().strip())
max_mut = 0
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if not jg_same_char(words[i], words[j]):
            max_mut = len(words[i]) * len(words[j])
print(max_mut)