#https://atcoder.jp/contests/abc172/tasks/abc172_b

s = input()
t = input()
count = 0
i = 0
while i < len(s):
    if s[i] != t[i]:
        count += 1
    i += 1
print(count)
