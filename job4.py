import random
L = []
M=[]
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
for i in L:
    for j in range(1,i+1):
        if i%j==0:
            M.append(j)
print(M)