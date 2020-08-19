#Developed by Devair Dener Darolt

import sympy as sy
import matplotlib.pyplot as plt
import numpy as np
 
pontos = [(-2.5,0.89), (-2.0,-1.18), (-1.5,1.88),(-1.0,4.06),(-0.5,1.21)]
#pontos =[ (-0.41,0), (0,2), (1.78,-4.75), (2.64,9.99)]
xs, ys = zip(*pontos)
ordem_polinomio = len(pontos)-1
lis = {}
soma = 0
polinomio_interpolador=''
def Li(x,index):
    global xs
    numerador =1
    denominador=1
    str_li='('
    for k in range(len(xs)):        
        if k !=index:            
            numerador *= (x-xs[k])
            if xs[k]<0:
                aux = abs(xs[k])
                str_li = str_li+ '(x + '+str(aux)+')'
            else:
                str_li = str_li+ '(x - '+str(xs[k])+')'                        
            denominador *=(xs[index]-xs[k])
    str_li=str_li+')/('      
            
    str_li = str_li + str(denominador)       
    str_li=str_li+')'      
 
    lis[index]=str_li
    #print('numerador:',numerador,'\ndenominador:',denominador)
    return numerador/denominador
 
 
def lagrange(x,pontos):
        
    global soma
    global polinomio_interpolador
    polinomio_interpolador+='P(x) = '
    # calcula os Li(x)
    for i in range(len(ys)):
        Li(x,i) # CALCULA LI --> L0 L1 L2 ... LK
        if ys[i]>0:
            polinomio_interpolador=polinomio_interpolador+" + "+str(ys[i])+" * ("+lis[i]+")"
        else:
            polinomio_interpolador=polinomio_interpolador+"  "+str(ys[i])+" * ("+lis[i]+")"
        soma=soma+ys[i]*Li(x,i)
    copy = polinomio_interpolador
    copy.replace(")","]")
    return soma
        
X=-2.5
print('p(',X,')=',lagrange(X,pontos))
print('\n',polinomio_interpolador.replace(")(",")*("),'\n')