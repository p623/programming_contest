N = int(input())

A = 0
W = 0
T = 0
R = 0

for i in range(N):
    S = input()
    if S == "AC":
        A+=1
    elif S == "WA":
        W+=1
    elif S == "TLE":
        T+=1
    elif S == "RE":
        R+=1

print("AC x " + str(A))
print("WA x " + str(W))
print("TLE x " + str(T))
print("RE x " + str(R))
