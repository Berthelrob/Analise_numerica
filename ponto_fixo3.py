# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x
import math
def f(x):    
    return x**3-11
 
def g(x):
    return x-((x**3-11)/3*x**2)
n = 10
a, b = [2, 3]
x0 = 2.1
for i in range(n):
    print('i:',i, '\t\traiz aproximada x:', x0)
    print('f(x): ',f(x0), '\tg(x):',g(x0))
    if(g(x0)<a or g(x0)>b):
        print('g(x) está fora do dominio [a,b] para x igual a ',x0)
        break
    if(x0 == g(x0)):
        print('\t\tPonto fixo: g(',x0,') = ',g(x0))
    xn = g(x0)
    x0 = xn
