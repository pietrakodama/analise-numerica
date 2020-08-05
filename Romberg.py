import numpy as np
import math 

def trapz(a,b,t,i,f): #formula n-trapezios
    h=(b-a)/2**i #define h_i
    if i==0:
        t_final=(f(a)+f(b))*(b-a)*0.5 #trapezio em um intervalo
    else:
        funcao=[]
        for j in range (1,2**(i-1)+1):
            funcao.append(f(a+(2*j-1)*h)) #define o somatorio da formula dos trapezios
        soma=sum(funcao)
        t_final=(t/2)+h*soma #trapezio em n-intervalos
    return (t_final) #retorna um valor numérico

def romb(a,b,n,E,f): #integracao pelo metodo de Romberg                                                                                             
    i=0                                                                                
    while i<=n+1:
        if i==0:
            T=[]
            T.append([trapz(a,b,T,i,f)]) #primeiro elemento de Romberg
            #print(T)
        if i>0 and i<=n+1:
            T.append([trapz(a,b,T[i-1][0],i,f)]) #primeira coluna de Romberg
            for k in range (1,i+1):
                T[i].append(T[i][k-1]+((T[i][k-1]-T[i-1][k-1])/(4**k-1))) #formula de Romberg

            if (abs(T[i][i]-T[i][i-1])<=E*abs(T[i][i])): #analise de precisao
                break    
        i=i+1 #proxima iteracao
    else:
        print("A integral nao converge para o numero maximo de linhas declarado")
        exit()
    return T,T[i][i],i

#define as funcoes testes e seus intervalos [a,b]

'''para outros valores de teste, basta modificar as f(x) definidas
com lambda e os respectivos intervalos de integracao'''                

f1=lambda x:x**2
a1=0
b1=1

f2=lambda x:1/(1-x)
a2=0
b2=0.995

f3=lambda x:1/(1+x**2)
a3=-5
b3=5

#aplica Romberg na f1
T,T_i,i=romb(a1,b1,20,10**(-8),f1)
print("Aproximacao da integral no intervalo",[a1,b1],":",T_i,".Na linha:",i)
'''
for p in range (i+1): #printa cada linha da tabela de Romberg
    print(T[p])
'''
#aplica Romberg na f2
T,T_i,i=romb(a2,b2,20,10**(-8),f2)
print("Aproximacao da integral no intervalo",[a2,b2],":",T_i,".Na linha:",i)
'''
for p in range (i+1): #printa cada linha da tabela de Romberg
    print(T[p])
'''
#aplica Romberg na f3
T,T_i,i=romb(a3,b3,20,10**(-8),f3)
print("Aproximacao da integral no intervalo",[a3,b3],":",T_i,".Na linha:",i)
'''
for p in range (i+1): #printa cada linha da tabela de Romberg
    print(T[p])
'''