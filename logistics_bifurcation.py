from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.animation as manimation
import copy

NUM_ITER = 1000
#Used to only investigate r(1-x)x at r=3
def ev(x,r=3):
    return r*(1-x)*x

def get_series(r):
    x = (r-1)/r
    dx = .000000001
    print(f"At {r=}, starting with {x=}+{dx}")
    x += dx
    record = []
    record.append(copy.copy(x))
    for i in range(NUM_ITER-1):
        x=ev(x,r)
        record.append(copy.copy(x))
    return record

def easy_logspace(start, stop, **kwargs):
    return np.logspace(np.log10(start), np.log10(stop), **kwargs)

def reversed_logspace(start, stop, **kwargs):
    short_of = easy_logspace(start, stop, **kwargs)[::-1] - stop
    return (start + -short_of[::-1])[::-1]

if __name__=="__main__":
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='simple_sweep', artist='Matplotlib', comment='bifurcation before reaching level 2')
    writer = FFMpegWriter(fps=20, metadata=metadata)
    fig, ax = plt.subplots()
    scat = ax.scatter(np.arange(NUM_ITER), np.linspace(0,1,NUM_ITER), marker="+")
    # r = 3.4158
    # r = 3.83
    #at r = 1.00001: slowly approaches solution
    #at r = 2: single step approach to solution.
    #at r = 2.99999: oscillatory approach to solution.
    with writer.saving(fig, "simple_sweep.mp4", 300):
        for r in reversed_logspace(2.9,3.84,num=200):
            scat.set_offsets(ary([np.arange(NUM_ITER), get_series(r)]).T)
            ax.set_title(f"{r=}")
            if np.isclose(r, 3.83, atol=1E-2):
                ax.set_title(rf"{r=},$\approx$ period 3!")
            writer.grab_frame()
        fig.clf()
    # dr = 0.019
    # due to rounding error, this bifurcation occurs at slightly earlier than 3.
    #at r = 3.83: period 3!