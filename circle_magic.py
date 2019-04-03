import numpy as np
import math

def Pi_tester(N):
    x=np.random.uniform(-1,1, N)
    y=np.random.uniform(-1,1, N)
    sum_sqr=x*x+y*y
    a=[]
    for val in sum_sqr:
        if math.sqrt(val)<=1:
            a.append(val)
    M=len(a)
    return (M/N)*4

print(Pi_tester(999))