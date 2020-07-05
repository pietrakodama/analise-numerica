import numpy as np
import math
from matplotlib import pyplot as plt

#decomposição LDLt 
def decomposicao (n,p,q,o): #decomposição para uma matriz tridiagonal simétrica (2 vetores)
    d=list(range(n)) 
    l=list(range(n-1))
    d[0]=p[0]
    for i in range(1,n):
        l[i-1]=q[i-1]/d[i-1] 
        d[i]=p[i]-(l[i-1]**2)*d[i-1] 
    m=len(p) #tamanho da diagonal principal
    y=list(range(m))
    z=list(range(m))
    w=list(range(m))
    y[0]=o[0]
    for i in range(1,m): 
        y[i]=o[i]-l[i-1]*y[i-1]         
    for i in range(m):
        z[i]=y[i]/d[i]
    w[m-1]=z[m-1]
    for i in range(m-2,-1,-1): 
        w[i]=z[i]-l[i]*w[i+1]
    return w 

#define a phi
def phi(s,i):
    if s>=x[i-1] and s<=x[i]:
        phi_i=(s-x[i-1])/h
    elif s>=x[i] and s<=x[i+1]:
        phi_i=(x[i+1]-s)/h
    else:
        phi_i=0
    return phi_i

#define a somatória de c_i*phi_i
def soma_sol(n,k):
    solucao_aprox=[]
    for i in range(1,n+1):
        solucao_aprox.append(c[i-1]*(phi(k,i))) 
    soma=sum(solucao_aprox)
    return soma

#define o erro 
def erro(n,g,j):
    e=[]
    for i in range(10*n+1):
        e.append(abs(g[i]-j[i]))
    e_max=np.max(e)
    return e_max

k=np.array([15,31,63,127,255])
vetor_ERRO=[]
for n in k:
    h=1/(n+1)
    #define x
    x=[]
    for i in range(n+2):
        x.append(i*h)
    
    '''print(x)'''
    
    #define o sistema Ac=di
    diag_principal=[] #diagonal principal da matriz tridiagonal A
    for i in range(1,n+1):
        diag_principal.append((1/h**2)*(x[i+1]-x[i-1]+((math.pi)**2)*(-(x[i]**2)*x[i-1]+x[i]*(x[i-1]**2)-((x[i-1]**3)/3)+(x[i+1]**3)/3+(x[i]**2)*x[i+1]-x[i]*(x[i+1]**2))))
    
    diag_secundaria=[] #diagonal secundária da matriz tridiagonal A
    for i in range (1,n):
        diag_secundaria.append((-1/h**2)*(x[i+1]-x[i])+(((math.pi)**2)/h**2)*((x[i+1]**3)/6-((x[i]*(x[i+1]**2))/2)-(x[i]**3)/6+(((x[i]**2)*x[i+1])/2)))

    F1=lambda x:(-2)*(math.pi)*x*(math.cos(x*math.pi))+2*math.sin(x*math.pi)#integral de xf(x)
    F2=lambda x:(-2)*(math.pi)*math.cos(x*math.pi) #integral de f(x)
    di=[]
    for i in range(1,n+1):
        di.append((1/h)*(F1(x[i])-F1(x[i-1])-F1(x[i+1])+F1(x[i])-x[i-1]*(F2(x[i])-F2(x[i-1]))+x[i+1]*(F2(x[i+1])-F2(x[i]))))

    #calcula o ci pela decomposição
    c=decomposicao(n,diag_principal,diag_secundaria,di)

    '''
    print(diag_principal)
    print(diag_secundaria)
    print(di)
    print(c)
    '''

    #define o y_i
    yi=[]
    for i in range(10*n+1):
        yi.append(i/(10*n))

    '''print(yi)'''

    #define a solução aproximada
    vetor_sol_aprox=[]
    for i in range(10*n+1):
        vetor_sol_aprox.append(soma_sol(n,yi[i]))
    
    '''print(vetor_sol_aprox)'''

    #define a solução exata
    exata=lambda x:math.sin(x*math.pi)
    solucao_exata=[]
    for i in range (10*n+1):
        solucao_exata.append(exata(yi[i]))

    '''print(solucao_exata)'''

    ERRO=erro(n,solucao_exata,vetor_sol_aprox)
    vetor_ERRO.append(ERRO)
    print("O erro para",n,"é:",ERRO)

    '''#gráfico da solução numérica
    plt.plot(yi,vetor_sol_aprox) 
    plt.xlabel("y_i")
    plt.ylabel("solução aproximada")
    plt.title("solução numérica nos y_i")
    plt.show()'''

#teste de convergência
for i in range(1,len(vetor_ERRO)):
    print("Análise de convergência:",vetor_ERRO[i-1]/vetor_ERRO[i])

#gráfico do erro
plt.plot(k,vetor_ERRO) 
plt.xlabel("Número de pontos no interior do intervalo")
plt.ylabel("Erro")
plt.title("Variação do erro")
plt.show()

'''#gráfico da solução exata
plt.plot(yi,solucao_exata) 
plt.xlabel("y_i")
plt.ylabel("solução exata")
plt.title("solução exata nos y_i")
plt.show()''' #comparar com o gráfico da solução numérica