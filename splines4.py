class Point:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

def Spline(points):
    N   = len(points)-1
    h   =     [(points[i+1].x-points[i].x)      for i in range(N)]         
    b   =     [(points[i+1].y-points[i].y)/h[i] for i in range(N)]          
    ftt = [0]+[3*(b[i+1]-b[i])/(h[i+1]+h[i])    for i in range(N-1)]+[0]    
    A   =     [(ftt[i+1]-ftt[i])/(6*h[i])       for i in range(N)]          
    B   =     [ftt[i]/2                         for i in range(N)]          
    C   =     [b[i]-h[i]*(ftt[i+1]+2*ftt[i])/6  for i in range(N)]          
    D   =     [points[i].y                      for i in range(N)]          
    return A,B,C,D

def PrintSpline(points,A,B,C,D):
    for i in range(len(points)-1):
        func = '[' + str(points[i].x) + ',' + str(points[i+1].x) + '] f(x) = '
        components = []
        if A[i]:
            components.append(str(A[i])+'(x-'+str(points[i].x)+')^3')
        if B[i]:
            components.append(str(B[i])+'(x-'+str(points[i].x)+')^2')
        if C[i]:
            components.append(str(C[i])+'(x-'+str(points[i].x)+')')
        if D[i]:
            components.append(str(D[i]))
        if components:
            func += components[0]
            for i in range (1,len(components)):
                if components[i][0] == '-':
                    func += ' - '+components[i][1:]
                else:
                    func += ' + '+components[i]
            print(func)
        else:
            print(func+'0')


def run(points):
    print("Pontos: ")
    points = [Point(x,y) for x,y in points]
    for point in points:
        print("(" + str(point.x) + "," + str(point.y) + ")", end = " ")
    print("")
    print("Interpolação spline cubica:")
    print ("Pontos \t função:")
    A,B,C,D = Spline(points)
    PrintSpline(points,A,B,C,D)
    print("")

run([(-2,0.2),(-1,0.5),(1,0.5),(2,0.2)])

