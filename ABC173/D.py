n = int(input())
listA = list(map(int, input().split()))
listA.sort()
listA.reverse()

i = 0
indexer = 0
flag = 0
count = 0
while i < len(listA):
    if i == 0:
        count+= 0
        i+=1
    elif i == 1:
        count+=listA[indexer]
        indexer+=1
        i+=1
    else:
        count+=listA[indexer]
        if flag:
            indexer+=1
            flag = 0
        else:
            flag = 1
        i+=1
print(count)



