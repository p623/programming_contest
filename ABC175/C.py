x, k, d = map(int, input().split())

a = (x + d*k)//(2*d)
b = a+1

if abs(x+d*k-2*d*a) < abs(x+d*k-2*d*b):
    best = a
else:
    best = b

if 0 <= best <= k:
    print(abs(x+d*k-2*d*best))
elif best < 0:
    print(abs(x+d*k))
else:
    print(abs(x-d*k))
