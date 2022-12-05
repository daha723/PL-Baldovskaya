f=open('C:\Users\79000\OneDrive\Рабочий стол\Балдовская Дарья Александровна_УБ-21_vvod.txt',"r")
s=open('C:\Users\79000\OneDrive\Рабочий стол\Балдовская Дарья Александровна_УБ-21_vivod.txt',"w")
A=[]
for line in f:
    a=list(map(int,line.split()))
    A.append(a)
s.write("Задание 8.1\n")
for i in range(1,5,2):
    D=[]
    for j in range(9):
            D.append(A[i][j])
    s.write("Минимальный элемент ")
    s.write(str(i+1))
    s.write(" строки: ")
    s.write(str(min(D)))
    s.write("\n")
max=0
c=k=l=m=0
min=10**10
for i in range(5):
    for j in range(9):
        if A[i][j]>max:
            max=A[i][j]
            c=i
            k=j
        if A[i][j]<min:
            min=A[i][j]
            l=i
            m=j
A[c][k],A[l][m]=A[l][m],A[c][k]
s.write("Задание 8.2\n")
s.write("Преобразованная матрица\n")
for i in range(5):
    for j in range(9):
        s.write(str(A[i][j]))
        s.write(" ")
    s.write("\n")
s.close()
f.close()
  