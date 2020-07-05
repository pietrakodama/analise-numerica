import numpy as np
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

#define a solução aproximada
def soma_sol(k):
    solucao_aprox=[]
    for i in range(1,n+1):
        solucao_aprox.append(c[i-1]*(phi(k,i))) 
    soma=sum(solucao_aprox)
    return soma

#define o erro 
def erro(n,g,j):
    e=[]
    for i in range(0,n+2):
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

    #define o sistema Ac=di
    diag_principal=[] #diagonal principal da matriz tridiagonal A
    for i in range(1,n+1):
        diag_principal.append((1/h**2)*(x[i+1]-x[i-1]))

    diag_secundaria=[] #diagonal secundária da matriz tridiagonal A
    for i in range (1,n):
        diag_secundaria.append((-1/h**2)*(x[i+1]-x[i]))

    di=[]
    for i in range(1,n+1):
        di.append((1/h)*(x[i]**2+(x[i-1]**2)/2+(x[i+1]**2)/2-(x[i+1]*x[i])-x[i]*x[i-1]))

    #calcula o ci pela decomposição
    c=decomposicao(n,diag_principal,diag_secundaria,di)

    '''
    print(diag_principal)
    print(diag_secundaria)
    print(di)
    print(c)
    '''

    vetor_sol_aprox=[]
    for i in range(0,n+2):
        vetor_sol_aprox.append(soma_sol(x[i]))
        
    #define a solução exata
    exata=lambda x:x*(1-x)/2
    solucao_exata=[]
    for i in range (0,n+2):
        solucao_exata.append(exata(x[i]))

    ERRO=erro(n,solucao_exata,vetor_sol_aprox)
    vetor_ERRO.append(ERRO)
    print("O erro para",n,"é:",ERRO)

'''#gráfico do erro
plt.plot(k,vetor_ERRO) 
plt.xlabel("Número de pontos no interior do intervalo")
plt.ylabel("Erro")
plt.title("Variação do erro")
plt.show()'''