from random import *
M=int(input("Введите количество строк "))
N=int(input("Введите количество столбцов "))
A=[]
for i in range(M):
    B=[]
    for j in range(N):
        B.append(randint(0,100))
    A.append(B)
for i in range(M):
     for j in range(N):
          print(A[i][j],end=" ")
     print()
for i in range(1,M,2):
    D=[]
    for j in range(N):
            D.append(A[i][j])
    print("Минимальный элемент",i+1,"строки:",min(D))