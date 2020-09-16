n = 

h = 1/(n+1)

x = []
for i in range (n+2):
  x.append(i*h)

### define a funcao B ###
def B (x):
  if x >= -2 and x < -1:
    funcaoB = (1/4)*(2+x)**3
  if x >= -1 and x < 0:
    funcaoB = (1/4)*((2+x)**3-4*(1+x)**3)
  if x >= 0 and x < 1:
    funcaoB = (1/4)*((2-x)**3-4*(1-x)**3)
  if x >= 1 and x <= 2:
    funcaoB = (1/4)*(2-x)**3
  else:
    funcaoB = 0
  return funcaoB

### define a derivada da funcao B ###
def derivada_B (x):
  if x >= -2 and x < -1:
    del_B = (3/4)*(2+x)**2
  if x >= -1 and x < 0:
    del_B = (3/4)*((2+x)**2-4*(1+x)**2)
  if x >= 0 and x < 1:
    del_B = (3/4)*(-(2-x)**2+4*(1-x)**2)
  if x >= 1 and x <= 2:
    del_B = (-3/4)*(2-x)**2
  else:
    del_B = 0
  return del_B

### define a funcao phi ###
def phi (x, i):
  if i == 0:
    phi_i = B((x-i*h)/h)-4*B((x+h)/h)
  if i == 1:
    phi_i = B((x-i*h)/h)-B((x+h)/h)
  if i >= 2 and i <= (n-1):
    phi_i = B((x-i*h)/h)
  if i == n:
    phi_i = B((x-i*h)/h)-B((x-(n+2)*h)/h)
  if i == n+1:
    phi_i = B((x-i*h)/h)-4*B((x-(n+2)*h)/h)
  return phi_i

### define a derivada da funcao phi ###
def derivada_phi (x, i):
  if i == 0:
    del_phi_i = derivada_B((x-i*h)/h)-4*derivada_B((x+h)/h)
  if i == 1:
    del_phi_i = derivada_B((x-i*h)/h)-derivada_B((x+h)/h)
  if i >= 2 and i <= (n-1):
    del_phi_i = derivada_B((x-i*h)/h)
  if i == n:
    del_phi_i = derivada_B((x-i*h)/h)-derivada_B((x-(n+2)*h)/h)
  if i == n+1:
    del_phi_i = derivada_B((x-i*h)/h)-4*derivada_B((x-(n+2)*h)/h)
  return del_phi_i
