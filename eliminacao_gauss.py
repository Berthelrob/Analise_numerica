import numpy as np

#Developed by Devair Dener Darolt

def Superior(A, b):
  Ln = len(b)
  cn = Ln
  for Li in range(0, Ln-1, 1):
    A[:], b[:] = pivo(Li, b, A)
    for Lj in range(Li+1, Ln, 1):
      lam   =  A[Lj][Li] /A[Li][Li]
      b[Lj] = b[Lj] - b[Li] * lam
      for ci in range(Li, cn, 1):
        A[Lj][ci] =  A[Lj][ci] - A[Li][ci] * lam
  return (b, A)
  
def pivo(k, b, A):
  print ('Entrou: pivotando a linha', k)
  print (A)
  n = len(b)
  jmax = k
  for j in range(k+1, n, 1):
    if ( np.abs(A[j][k]) > np.abs(A[jmax][k]) ):
      jmax = j
 
  TempA       = np.zeros_like(b)
  TempA[:]    = A[k][:]
  A[k][:]     = A[jmax][:]
  A[jmax][:]  = TempA[:]
   
  TempB  = b[k]
  b[k]   = b[jmax]
  b[jmax] = TempB
   
  print ('linha', k, 'trocou com', jmax)
  print (A, '\n')
 
  return A, b

def retrosub(b, A):
  n = len(b)
  x = np.zeros_like(b)
  x[n-1] = b[n-1] / A[n-1][n-1]
   
  for i in range(n-2, -1, -1):
    soma = b[i]
    for j in range(i+1, n, 1):
      soma = soma - A[i][j]*x[j]
    x[i] = soma / A[i][i]     
  return x

A = [[3,2,1],[2,7,2],[1,3,5]]
b = [2,-3,3]
b, A = Superior(A, b)
print(A)
x = retrosub(b, A) 
print ('\nA solução é:')
for i in range(len(x)):
  print('x',str(i+1),'=',x[i],'\t')
  