s = input()

count = 0
bef = ""
maxC = 0
for i in range(len(s)):
    if bef == "" and s[i] == "R":
        count += 1
    else:
        if s[i] == "R" and bef == "R":
            count += 1
        elif s[i] == "R" and bef == "S":
            if count > maxC:
                maxC = count
            count = 1
        elif s[i] == "S" and bef == "R":
            if count > maxC:
                maxC = count
            count = 0
        else:
            count = 0
    bef = s[i]
if count > maxC:
    maxC = count
print(maxC)

        

        
