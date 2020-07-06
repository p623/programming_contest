n, k = map(int, input().split())
listA = list(map(int, input().split()))
zeroFlag = 0
if 0 in listA:
    zeroFlag = 1
    listA.remove(0)
listA.sort()

hidariI = 0
migiI = len(listA)-1

hidatiKouho = 1
migiKouho = 1

for i in range(k):
    hidatiKouho*=listA[hidariI]
    migiKouho*=listA[migiI]
    if hidatiKouho > 0:
        hidatiKouho %= 10**9 + 7
    if migiKouho > 0:
        migiKouho %= 10**9 + 7
    hidariI+=1
    migiI-=1

if zeroFlag:
    print(max(hidatiKouho, migiKouho, 0)%(10**9 + 7))
else:
    print(max(hidatiKouho, migiKouho) % (10**9 + 7))

