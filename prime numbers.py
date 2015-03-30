def primeCheck(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
 
pList=[]
for i in range(3, 1000):
     if primeCheck(i):
         pList.append(i)

print pList, sum(pList)
            