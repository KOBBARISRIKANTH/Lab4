import random
L = []
M=[]
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
SUM=0
for element in L:
    if element%2==0:
        M.append(element)
        SUM=SUM+element
print("List of even numbers is :",M)
print("The sum of even numbers is:",SUM)

