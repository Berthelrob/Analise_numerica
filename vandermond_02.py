import numpy as np
def f(x):
    return x**x
 
pontos =[(0.99,f(0.99)), (1,f(1)), (1.01,f(1.01))]
 
n = len(pontos)
def vandermond(pontos):
    xs, ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A, B)
    return a
 
a = vandermond(pontos)
 
def p(x):
    px = sum([a[k] * x ** k for k in range(n)])
    return px
 
def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'
 
def equation(pontos):
    eq = "p(x)="
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq
 
eq = equation(pontos)
print(eq)