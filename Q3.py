import library as inte
import math
def f(x):
    return math.e**(-(x)**2)
print("***********************************************************************************************************************")
maxerror=0.001
I=0.746824133 #from wolfram alpha
print("The analytical value obtained for the integral is ",I)
print("Method              Value of the Integral             Number of iterations")
N=2
while abs(inte.midpoint(0,1,N,f)-I)>=maxerror:
    N+=1
j=inte.midpoint(0,1,N,f)
print("Midpoint              "+str(j)+"                "+str(N))
N=2
while abs(inte.trapezoid(0,1,N,f)-I)>=maxerror:
    N+=1
j=inte.trapezoid(0,1,N,f)
print("Trapezoid              "+str(j)+"              "+str(N))
N=2
while abs(inte.simpson(0,1,N,f)-I)>=maxerror:
    N+=1
j=inte.simpson(0,1,N,f)
print("Simpsons              "+str(j)+"               "+str(N))
print("***********************************************************************************************************************")
'''output
***********************************************************************************************************************
The analytical value obtained for the integral is  0.746824133
Method              Value of the Integral             Number of iterations
Midpoint              0.747677083350702                6
Trapezoid              0.7458656148456951              8
Simpsons              0.7471804289095103               2
***********************************************************************************************************************
'''