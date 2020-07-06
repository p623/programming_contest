import itertools

data = [0, 1]

h, w, k = map(int, input().split())
countA = 0
gyoL = [0]*h  # 1gyo, 2gyo...
retuL = [0]*w  # 1retu, 2retu...
cL = []
for i in range(h):
    inputL = list(input())
    countSum = 0
    for l in range(w):
        if inputL[l] == "#":
            countA+=1
            countSum += 1
            retuL[l] += 1
    gyoL[i] = countSum
    cL.append(inputL)

gyo = list(itertools.product(data, repeat=h))
retu = list(itertools.product(data, repeat=w))

ansC = 0
for tG in gyo:
    for tR in retu:
        count = countA
        gOneL = []
        rOneL = []
        for index1 in range(len(tG)):
            if tG[index1] == 1:
                count-=gyoL[index1]
                gOneL.append(index1)
        for index2 in range(len(tR)):
            if tR[index2] == 1:
                count-=retuL[index2]
                rOneL.append(index2)
        for g in gOneL:
            for r in rOneL:
                if cL[g][r] == "#":
                    count += 1
        if count == k:
            ansC+=1
print(ansC)
        
