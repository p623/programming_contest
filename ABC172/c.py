#https://atcoder.jp/contests/abc172/tasks/abc172_c

n, m, k = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

sumAL = [0]
for i in range(len(listA)):
    sumAL.append(sumAL[-1]+listA[i])
sumBL = [0]
for i in range(len(listB)):
    sumBL.append(sumBL[-1]+listB[i])
ib = len(sumBL)-1
bookMax = 0
for ia in range(len(sumAL)):
    while ib > -1:
        if sumBL[ib] <= k-sumAL[ia]:
            if bookMax < ia+ib:
                bookMax = ia+ib
            break
        ib-=1
print(bookMax)


