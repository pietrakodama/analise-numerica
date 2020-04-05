#Método de Newton para aproximações de raízes de funcões univariadas

import math

#defina aqui a função
def f(x): 
        return 2*x**2+3*x-2

#defina aqui a derivada
def derivada(x): 
        return 4*x+3

#definição do método de Newton
def newton(f, derivada, x0, epsilon, max_iter=50):
    if abs(f(x0))<=epsilon:
        return x0
    print ("k\t x0\t\t fx(x0)") #\t é o espaçamento 

    #aplicação do método de Newton
    k=1 #número de iterações
    while k<=max_iter:
        x1=x0-(f(x0)/derivada(x0))       
        print ("%d\t%e\t%e" %(k,x1,f(x1)))

        if abs(f(x1))<=epsilon:
            return x1
        #recebe novas variáveis se a condição não for satisfeita
        x0=x1                             
        k=k+1
    print ("ERRO: número máximo de iterações atingido")

    return x1

#defina o chute inicial e o epsilon (erro)
raiz = newton(f,derivada,1.0,0.0001)        
print(raiz)
