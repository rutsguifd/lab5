x=float(input())
eps=float(input())
suma=0
k=1
while el>eps:
    el = (x ** k) / (k)
    suma+=el
    k+=1
rs=suma-(x**k)/(k)
print(rs)
print(k)