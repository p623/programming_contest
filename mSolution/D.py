n = int(input())
listA = list(map(int, input().split()))

memo = {}

def solve(mon, i, haveN):
    key = str(mon) + " " + str(i) + " " + str(haveN)
    if key in memo:
        return memo[key]
    if i >= len(listA):
        memo[key] = 0
        return memo[key]
    elif i == len(listA)-1:
        mon+=haveN*listA[i]
        haveN=0
        memo[key] = mon
        return memo[key]
    else:
        memo[key] =  max(solve(mon, i+1, haveN), solve(mon-listA[i]*(mon//listA[i]), i+1, haveN+mon//listA[i]), solve(mon+haveN*listA[i], i+1, 0))
        return memo[key]
        
print(solve(1000, 0, 0))
    
