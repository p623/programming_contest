a, b, c = map(int, input().split())
k = int(input())

count = 0

while count <= k:
    if a < b and b < c:
        break
    if a >= b:
        count+=1
        b*=2
    elif b >= c:
        count+=1
        c*=2
if a < b and b < c and count <= k:
    print("Yes")
else:
    print("No")
