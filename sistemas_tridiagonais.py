n=int(input("Entre com a dimensão da matriz A: "))
a=list(range(n)) #diagonal da matriz A
print("Entre com os elementos da diagonal de A: ")
for i in a:
    a[i]=float(input())

b=list(range(n-1)) #subdiagonal da matriz A
print("Entre com os elementos da subdiagonal de A: ")
for i in b:
    b[i]=float(input())

d=list(range(n)) #vetor d com dimensão n
l=list(range(n-1)) #vetor l com dimensão n-1

def decomp (a,b): #rotina da decomposição
    d[0]=a[0]
    for i in range(1,n):
        l[i-1]=b[i-1]/d[i-1] #entradas do vetor l da matriz L da decomposição
        d[i]=a[i]-(l[i-1]**2)*d[i-1] #entradas do vetor d da matriz D da decomposição
    return l,d  

L,D =decomp (a,b)  

print("O vetor representando L é: ", L)
print("O vetor representando D é: ", D)

v=list(range(n))

print("Entre com o valores do vetor b do sistema linear Ax=b: ")
for i in v:
    v[i]=float(input())                    

#vetores (dimensão n) para resolver o sistema
y=list(range(n))
z=list(range(n))
x=list(range(n))

def resolve_sistema(v): #rotina que resolve o sistema linear Ax=v com A tridiagonal simétrica            
    n=len(a)
    y[0]=v[0]
    for i in range(1,n): #vai do 1 até o n-1
        y[i]=v[i]-l[i-1]*y[i-1]         
    
    for i in range(n):
        z[i]=y[i]/d[i]
    x[n-1]=z[n-1]

    for i in range(n-2,-1,-1): #vai do n-1 até o 0 
        x[i]=z[i]-l[i]*x[i+1]
    
    return (x)

sol=resolve_sistema(v)
print("o vetor solução do sistema é: " ,sol)
