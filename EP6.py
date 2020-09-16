import numpy as np
import math

def decomposicao (n, dprincipal, dsecundaria, vetor_igualdade): #decomposição para uma matriz tridiagonal simétrica (2 vetores)
    d = list(range (n)) 
    l = list(range (n-1))
    d[0] = dprincipal[0]
    for i in range (1,n):
        l[i-1] = dsecundaria[i-1]/d[i-1] 
        d[i] = dprincipal[i]-(l[i-1]**2)*d[i-1] 
    m = len (dprincipal) #tamanho da diagonal principal
    y = list(range (m))
    z = list(range (m))
    w = list(range (m))
    y[0] = vetor_igualdade[0]
    for i in range (1,m): 
        y[i] = vetor_igualdade[i]-l[i-1]*y[i-1]         
    for i in range (m):
        z[i] = y[i]/d[i]
    w[m-1] = z[m-1]
    for i in range (m-2,-1,-1): 
        w[i] = z[i]-l[i]*w[i+1]
    return w 

def trapz (a, b, t, i, f): #formula n-trapezios
    h = (b-a)/2**i #define h_i
    if i == 0:
        t_final = (f(a)+f(b))*(b-a)*0.5 #trapezio em um intervalo
    else:
        funcao = []
        for j in range (1,2**(i-1)+1):
            funcao.append(f(a+(2*j-1)*h)) #define o somatorio da formula dos trapezios
        soma = sum(funcao)
        t_final = (t/2)+h*soma #trapezio em n-intervalos
    return (t_final) #retorna um valor numérico

def romb (a, b, N, E, f): #integracao pelo metodo de Romberg                                                                                             
    i = 0                                                                                
    while i <= N+1:
        if i == 0:
            T = []
            T.append([trapz(a,b,T,i,f)]) #primeiro elemento de Romberg
            #print(T)
        if i > 0 and i <= N+1:
            T.append([trapz(a,b,T[i-1][0],i,f)]) #primeira coluna de Romberg
            for k in range (1,i+1):
                T[i].append(T[i][k-1]+((T[i][k-1]-T[i-1][k-1])/(4**k-1))) #formula de Romberg

            if (abs(T[i][i]-T[i][i-1]) <= E*abs(T[i][i])): #analise de precisao
                break    
        i = i+1 #proxima iteracao
    else:
        print("A integral nao converge para o numero maximo de linhas declarado")
        exit()
    return T[i][i]
   
def soma_sol1 (k):
    solucao_aprox = []
    for i in range (1, n+1):
        solucao_aprox.append(alfa[i-1]*(phi(k,i))) 
    soma = sum(solucao_aprox)
    return soma

def soma_sol2 (n, k):
    solucao_aprox = []
    for i in range (1,n+1):
        solucao_aprox.append(alfa[i-1]*(phi(k,i))) 
    soma = sum(solucao_aprox)
    return soma

## elementos finitos ##

#### splines lineares para o sistema A*alfa = b ####
t = np.array([15,31,63,127,255])
for n in t:

    h = 1/(n+1)

    x = []
    for i in range (n+2):
        x.append(i*h)

    # print (x)

    #### defina as funções k(x) e q(x) para aplicação do metodo ####
    '''defina aqui k(x) e q(x)'''
    k = k 
    q = q
    f1 = lambda x: k
    f2 = lambda x: q*((x-i*h+h)**2)
    f3 = lambda x: q*((i*h+h-x)**2)
    f4 = lambda x: k-(q*(i*h+h-x)*(x-i*h))

    diag_principal = [] # diagonal principal da matriz A
    for i in range (1, n+1):
        diag_principal.append((1/h**2)*(romb(x[i-1], x[i+1], 20, 10**(-6), f1)+romb(x[i-1], x[i], 20, 10**(-6), f2)+romb(x[i], x[i+1], 20, 10**(-6), f3)))

    # print (diag_principal)

    diag_secundaria = [] # diagonal secundaria da matriz A
    for i in range (1, n):
        diag_secundaria.append((-1/h**2)*(romb(x[i], x[i+1], 20, 10**(-6), f4)))

    # print (diag_secundaria)

    ### vetor b do sistema ###

    '''defina aqui a f(x)'''
    f1x = lambda x: f*(x-i*h+h) 
    f2x = lambda x: f*(i*h+h-x)

    vetor_b = []
    for i in range (1, n+1):
        vetor_b.append((1/h)*(romb(x[i-1],x[i],20,10**(-6),f1x)+romb(x[i],x[i+1],20,10**(-6),f2x)))

    # print (vetor_b)

    ### solução pela decomposição ####

    alfa = decomposicao(n, diag_principal, diag_secundaria, vetor_b) #aplica a decomposição 

    # print (alfa)

    ### solução aproximada u_barra ###

    def phi (s, i): #define a phi
        if s >= x[i-1] and s < x[i]:
            phi_i = (s-x[i-1])/h
        elif s >= x[i] and s <= x[i+1]:
            phi_i = (x[i+1]-s)/h
        else:
            phi_i = 0
        return phi_i 

    u_barra1 = []
    for i in range (n+2):
        u_barra1.append(soma_sol1(x[i]))    
    
    yi = []
    for i in range (10*n+1):
        yi.append(i/(10*n))

    u_barra2 = []
    for i in range (10*n+1):
        u_barra2.append(soma_sol2(n,yi[i]))

    # print("A solucao aproximada usando x_i")    
    # print(u_barra1)
    # print("A solucao aproximada usando y_i")    
    # print(u_barra2)

    ### solução exata u ###
    exata = lambda x: (x**2)*(x-1)**2

    u1 = []
    for i in range (n+2):
        u1.append(exata(x[i]))
    
    u2 = []
    for i in range (10*n+1):
        u2.append(exata(yi[i]))

    ### erro ###
    def erro1(n,g,j):
        e = []
        for i in range (n+2):
            e.append(abs(g[i]-j[i]))
        e_max = np.max(e)
        return e_max

    def erro2(n,g,j):
        e = []
        for i in range(10*n+1):
            e.append(abs(g[i]-j[i]))
        e_max = np.max(e)
        return e_max

    ERRO1 = erro1(n, u1, u_barra1)
    ERRO2 = erro2(n, u2, u_barra2)
    print("O erro para",n," com x_i é:",ERRO1,"e com y_i é:",ERRO2)
