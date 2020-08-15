n = int(input())
listL = list(map(int, input().split()))

count = 0
for l1 in listL:
    for l2 in listL:
        for l3 in listL:
            if l2 > l1 and l3 > l2 and l1+l2 > l3:
                count += 1
print(count)
