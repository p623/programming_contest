n, k = map(int, input().split())
listA = list(map(int, input().split()))

i = k
while i < len(listA):
    if listA[i] > listA[i-k]:
        print("Yes")
    else:
        print("No")
    i+=1

