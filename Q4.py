import library as lib
def f(x):
    return 4/(1+x**2)
file = open("Q4_datapoints.txt", "w+")
for N in range(1,10000):
    file.writelines([str(N)+" ",str(lib.montecarlo(0,1,N,f))+"\n"]) 
file.close()