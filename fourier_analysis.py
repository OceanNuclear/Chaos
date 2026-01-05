import numpy as np
from tqdm import tqdm
import seaborn as sns
from matplotlib import pyplot as plt

SEQ_LENGTH = 10000
SKIP_INITIAL= 1000
START_VAL = 0.5

def ev(x,r=3):
    return r*(1-x)*x

def dy_dx(y, r):
    y_new = ev(y, r)
    return y_new-y

def take_step(y, r, step_size=1):
    #y must be a scalar
    return y+dy_dx(y, r)*step_size

def make_series(r, start_x=START_VAL, series_length=SEQ_LENGTH):
    y_list = [start_x,]
    for i in range(SEQ_LENGTH-1):
        y_list.append(take_step(y_list[-1], r))
    return y_list

def fourier_analyse(y, max_intervals):
    seq_length = len(y)
    if max_intervals > seq_length:
        raise ValueError(
            "The required Fourier analysis wavelength is lower "
            "than the minimum sampling frequency!"
        )
    n = np.arange(seq_length)
    magnitude = [abs(sum(y))/seq_length,]
    for num_samples_per_cycle in range(1, max_intervals+1):
        frequency = np.pi/num_samples_per_cycle
        cos_integral = (np.cos(frequency * n) * y).sum()
        sin_integral = (np.sin(frequency * n) * y).sum()
        mag_i = np.sqrt(abs(cos_integral)**2 + abs(sin_integral)**2)
        magnitude.append(mag_i/seq_length)
    return np.array(magnitude)

if __name__=='__main__':
    log_map_frequency_plot = []
    for r in tqdm(np.linspace(3.842, 3.850, 100), desc="Running r="):
        series = make_series(r)[SKIP_INITIAL:]
        fourier_ans = fourier_analyse(series, 20)
        fourier_ans = fourier_ans[1:]/fourier_ans.max()
        log_map_frequency_plot.append(fourier_ans.copy())
    sns.heatmap(np.array(log_map_frequency_plot).T)
    plt.show()