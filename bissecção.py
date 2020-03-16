import math

#definir o intervalo [a,b] e o erro e
a=float(input("Digite a extremidade inferior do intervalo:"))
b=float(input("Digite a extremidade superior do intervalo:"))
e=float(input("Digite o erro:"))

#definir uma função
def f(x):
    return x**2-2

#teorema de Bolzano
#math.fabs (módulo)
if f(a)*f(b)<0:
    while (math.fabs(b-a)/2>e):
        xi=(a+b)/2
        if f(xi)==0:
            print("A raíz é:",xi)
            break
        else: #teorema de Bolzano de novo pra ver qual o novo intervalo
            if f(a)*f(xi)<0:
                b=xi
            else:
                a=xi
    print("A raíz é:",xi)

else:
    print("Não há raíz neste intervalo.")
