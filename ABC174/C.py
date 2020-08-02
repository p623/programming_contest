k = int(input())
valM = {}
count = 0
flag = 1
amari = 0
while True:
    count += 1
    amari = (amari*10+7) % k
    if (amari in valM):
        break
    if amari == 0:
        print(count)
        flag = 0
        break
    else:
        valM[amari] = 0
if flag:
    print("-1")
