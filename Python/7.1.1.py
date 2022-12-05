def F(n):
    c=0
    k=n
    while k>0:
        l=len(str(n))
        c+=(k%10)**l
        k//=10
    if c==n:
        return c
k=int(input("Введите число, до которого необходимо перебирать числа "))
for i in range(1,k+1):
    if F(i) is not None:
        print(F(i),"Является числом Армстронга")