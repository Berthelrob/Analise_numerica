# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x

#def g(x):
#    return (x + 7 / x) / 2
def f(x):
    #return x**3 + 8*x-7
    return x**2-7

def g(x):
	#return (7-x**3)/8
    return 1/2*(x+7/x)

n = 10
a, b = [2, 3]
x0 = 2
for i in range(10):
    print('i:',i, '\t\traiz aproximada:', x0, ' \t\t\tf(x): ',f(x0))
    print('i:',i, '\t\tPonto fixo: g(',x0,') = ',g(x0))
    xn = g(x0)
    x0 = xn
    
