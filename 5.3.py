x=float(input())
eps=float(input())
suma=0
k=1
while suma<eps:
    suma+=(x**k)/(k)
    k+=1
rs=suma-(x**k)/(k)
print(rs)
print(k)
