import numpy as np

n = int(input('Entre com a dimensao da matriz:'))
erro = float(input('Entre com o erro:'))

def metodoSOR(x,omega,erro,matriz_inicial):
    criterio_parada = 100   #criterio de parada inicial 
    quantidade_iteracoes = 0    #contador de iterações 
    T = matriz_inicial.copy()
    T_anterior = matriz_inicial.copy()  #matriz que armazena as iterações

    while criterio_parada > erro and quantidade_iteracoes < 500:
        quantidade_iteracoes = quantidade_iteracoes + 1
        for i in range(1,n):
            for j in range(1,n):
                T[i][j]=((1-omega)*T_anterior[i][j])+((omega/4)*(T[i-1][j]+T[i+1][j]+T[i][j-1]+T[i][j+1]))
        S = T - T_anterior
        criterio_parada = abs(max(S.min(), S.max(), key=abs))   #norma infinita pra avaliar o erro
        T_anterior = T.copy()

    return(quantidade_iteracoes,T)
 
#definição da matriz T com chute inicial nulo
T = np.zeros ((n+1,n+1))
for i in range(n+1):
  T[i][0]=-3  
for j in range(n+1):
  T[0][j]=-3
for i in range(n+1):
  T[i][n]=((6*(i)/n)-3)
for j in range(n+1):
  T[n][j]=((6*(j)/n)-3)

#definição do ômega
omega = np.zeros(101)   
for i in range (101):
    W = 1+(i/100)
    omega[i] = W       

iteracoes_zeros = np.zeros(101) #quantidade de iterações com chute inicial nulo

#SOR com o chute nulo
for i in range (101):     
    iteracoes,Z = metodoSOR(n,omega[i],erro,T)  #varia o ômega a cada iteração 
    iteracoes_zeros[i] = iteracoes

#menor numero de iterações para o chute nulo
quant_iter_zeros = 1
for i in range (100):
    if iteracoes_zeros[i] > iteracoes_zeros[i+1] :
        if quant_iter_zeros != iteracoes_zeros[i+1]:
            qual_omega_zeros = omega[i+1]
            posicao_omega_zeros = i+1
            quant_iter_zeros = iteracoes_zeros[i+1]

print('O omega',posicao_omega_zeros,'igual a',qual_omega_zeros,'resulta em',quant_iter_zeros,'iteracoes para o chute inicial nulo.')


#definição da T com chute inicial aleatório entre 0 e 1
T1 = T.copy()
for i in range(1,n):
    for j in range(1,n):
        T1[i][j] = np.random.random_sample(1)   #altera os valores do chute inicial entre 0 e 1

iteracoes_aleatorio = np.zeros(101) #quantidade de iterações com chute inicial aleatório entre 0 e 1

#SOR com o chute inicial aleatório entre 0 e 1 
for i in range (101):
    iteracoes,Z = metodoSOR(n,omega[i],erro,T1)
    iteracoes_aleatorio[i] = iteracoes

#menor numero de iterações para o chute inicial aleatório entre 0 e 1
quant_iter_aleatorio = 1
for i in range (100):
    if iteracoes_aleatorio[i] > iteracoes_aleatorio[i+1] :
        if quant_iter_aleatorio != iteracoes_aleatorio[i+1]:
            qual_omega_aleatorio = omega[i+1]
            posicao_omega_aleatorio = i+1
            quant_iter_aleatorio = iteracoes_aleatorio[i+1]

print('O omega',posicao_omega_aleatorio,'igual a',qual_omega_aleatorio,'resulta em',quant_iter_aleatorio,'iteracoes para o chute inicial com valores aleatorios entre 0 e 1.')

