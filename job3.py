import random
L = []
M=[]
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
SUM=0
for i in L:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt=cnt+1
    if cnt==2:
        M.append(i)
        SUM=SUM+i
print("The listof Prime Numbers is:",M)
print("The sum of Prime Numbers is:",SUM)