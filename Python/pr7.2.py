def F(x1,x2,y1,y2,z1,z2):
    cosx=x1/(x1**2+x2**2)**0.5
    cosy=y1/(y1**2+y2**2)**0.5
    cosz=z1/(z1**2+z2**2)**0.5
    d=max(cosx,cosy,cosz)
    if d==cosx:
        print("Координаты X точки",x1,x2," образуют минимальный угол")
    elif d==cosy:
        print("Координаты Y точки",y1,y2," образуют минимальный угол")
    else: print("Координаты Z точки",z1,z2," образуют минимальный угол")
x1,x2,y1,y2,z1,z2=map(float,input("Введите координаты 3 точек X,Y и Z (6 чисел через пробел) ").split())
F(x1,x2,y1,y2,z1,z2)