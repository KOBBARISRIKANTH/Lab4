
import random
L = []
M=[]
for i in range(50):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
for i in L:
    t=i
    revers=0
    while i>0:
        remainder=i%10
        revers=(revers*10)+remainder
        i=i//10
    if t==revers:
        M.append(t)
print(M)
