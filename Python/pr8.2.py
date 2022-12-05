from random import *
M=int(input("Введите количество строк "))
N=int(input("Введите количество столбцов "))
A=[]
for i in range(M):
    B=[]
    for j in range(N):
        B.append(randint(0,100))
    A.append(B)
print("Первоначальная матрица")
for i in range(M):
    for j in range(N):
        print(A[i][j], end=" ")
    print()
max=0
c=k=l=m=0
min=10**10
for i in range(M):
    for j in range(N):
        if A[i][j]>max:
            max=A[i][j]
            c=i
            k=j
        if A[i][j]<min:
            min=A[i][j]
            l=i
            m=j
A[c][k],A[l][m]=A[l][m],A[c][k]
print("Преобразованная матрица")
for i in range(M):
    for j in range(N):
        print(A[i][j], end=" ")
    print()