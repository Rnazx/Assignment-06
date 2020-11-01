import library as inte
def f(x):
    return x/(1+x)
print("***********************************************************************************************************************")
I=1.30685281944
print("The analytical value obtained for the integral is 2-ln(2)",I)
print("For N=6 :-")
N=6
print("Method              Value of the Integral             Error from Analytical value")
j=inte.midpoint(1,3,N,f)
print("Midpoint              "+str(j)+"              "+str(j-I))
j=inte.trapezoid(1,3,N,f)
print("Trapezoid              "+str(j)+"              "+str(j-I))
j=inte.simpson(1,3,N,f)
print("Simpsons              "+str(j)+"              "+str(j-I))
print("***********************************************************************************************************************")
print("For N=10 :-")
N=10
print("Method              Value of the Integral             Error from Analytical value")
j=inte.midpoint(1,3,N,f)
print("Midpoint              "+str(j)+"              "+str(j-I))
j=inte.trapezoid(1,3,N,f)
print("Trapezoid              "+str(j)+"              "+str(j-I))
j=inte.simpson(1,3,N,f)
print("Simpsons              "+str(j)+"              "+str(j-I))
print("***********************************************************************************************************************")
print("For N=26 :-")
N=26
print("Method              Value of the Integral             Error from Analytical value")
j=inte.midpoint(1,3,N,f)
print("Midpoint              "+str(j)+"              "+str(j-I))
j=inte.trapezoid(1,3,N,f)
print("Trapezoid              "+str(j)+"              "+str(j-I))
j=inte.simpson(1,3,N,f)
print("Simpsons              "+str(j)+"              "+str(j-I))
'''Output
***********************************************************************************************************************
The analytical value obtained for the integral is 2-ln(2) 1.30685281944
For N=6 :-
Method              Value of the Integral             Error from Analytical value
Midpoint              1.3077156791250208              0.000862859685020867
Trapezoid              1.3051226551226551              -0.001730164317344851
Simpsons              1.306830206830207              -2.2612609793082328e-05
***********************************************************************************************************************
For N=10 :-
Method              Value of the Integral             Error from Analytical value
Midpoint              1.3071646395900398              0.0003118201500398321
Trapezoid              1.306228596824572              -0.0006242226154280495
Simpsons              1.3068497693110697              -3.05012893031531e-06
***********************************************************************************************************************
For N=26 :-
Method              Value of the Integral             Error from Analytical value
Midpoint              1.3068990323038625              4.621286386252699e-05
Trapezoid              1.3067603809022115              -9.243853778850841e-05
Simpsons              1.3068527513069688              -6.813303121688818e-08
'''