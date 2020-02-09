from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
import copy

NUM_ITER = 80
#Used to only investigate r(1-x)x at r=3
def ev(x,r=3):
    return r*(1-x)*x

if __name__=="__main__":
    r = 3
    r -= 0.01
    dx = 0.000000001
    #at r = 1.00001: slowly approaches solution
    #at r = 2: single step approach to solution.
    #at r = 2.99999: oscillatory approach to solution.
    # due to rounding error, this bifurcation occurs at slightly earlier than 3.
    x = (r-1)/r
    x += dx
    record = []
    record.append(copy.copy(x))
    print("starting with x=", x)
    for i in range(NUM_ITER):
        x=ev(x,r)
        record.append(copy.copy(x))
    plt.plot(record)
    plt.show()