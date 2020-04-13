from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt
from logistics_bifurcation import ev

NUM_ITER = 5000
START_VAL = 0.01

def dy_dx(y, r):
    y_new = ev(y, r)
    return y_new-y

def take_step(y, r, step_size=1):
    #y must be a scalar
    return y+dy_dx(y, r)*step_size

if __name__=='__main__':
    step_size = 0.93
    r = 3.5
    y = [START_VAL,]
    for i in range(NUM_ITER-1):
        y.append(take_step(y[-1], r=r, step_size=step_size))

    plt.scatter(x:=np.linspace(0.0, step_size*float(NUM_ITER), NUM_ITER), y, marker='x')
    plt.show()
