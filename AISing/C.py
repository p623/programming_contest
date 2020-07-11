import math
n = int(input())

for i in range(n):
    top = int(math.sqrt(i))
    count = 0
    for x in range(top-1):
        for y in range(x+1):
            for z in range(y+1):
                if (x+1)**2 + (y+1)**2 + (z+1)**2 + (x+1)*(y+1) + (y+1)*(z+1) + (z+1)*(x+1) == i+1:
                    if x+1 == y+1 and y+1 == z+1:
                        count += 1
                    elif x+1 != y+1 and y+1 != z+1 and z+1 != x+1:
                        count += 6
                    else:
                        count += 3
    print(count)
