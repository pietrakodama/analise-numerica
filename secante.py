#Método da Secante para a aproximação de funcões univariáveis

import math

#defina aqui a função
def f(x): 				
	return 2*x**2+3*x-2  	

#definição do método da Secante
def secante(f,x0,x1,epsilon,max_iter=50): #defina aqui o número máximo de iterações

    #verifica se os chutes iniciais são soluções
    if abs(f(x0))<=epsilon: 
        return x0
    print ("k\t x\t\t f(x0)")
    if abs(f(x1))<=epsilon:
        return x1
    print ("k\t x\t\t f(x1)")

    #aplicação do método da secante
    k=1 #número de iterações
    while k<=max_iter:
        xn=x1-(f(x1)*((x1-x0)/(f(x1)-f(x0))))
        print ("%d\t%e\t%e" %(k,xn,f(xn)))

        if abs(f(xn))<=epsilon:
            return xn
        #recebe novas variáveis se a condição não for satisfeita
        x0=x1
        x1=xn
    print ("ERRO: número máximo de iterações atingido")

    return xn

#defina aqui os chutes iniciais x0 e x1 e o epsilon (erro)
raiz = secante(f,0,1.0,0.0001) 
print(raiz)
