n = int(input())
cA = input()

wCounter = 0
for i in range(n):
    if cA[i] == "W":
        wCounter += 1

flag = 0
count = 0
for i in range(n-1, -1, -1):
    if flag == 0 and cA[i] == "R":
        flag = 1
    if flag == 1 and i < n-wCounter and cA[i] == "W":
        count += 1
print(count)
