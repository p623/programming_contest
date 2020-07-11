n = int(input())
listA = list(map(int, input().split()))

count = 0
for i in range(len(listA)):
    if (i+1)%2 == 1 and listA[i]%2 == 1:
        count+=1
print(count)