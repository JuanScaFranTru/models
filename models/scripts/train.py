import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    filename = 'to_predict.csv'

    weeks = np.loadtxt(filename, delimiter=',', usecols=0, dtype=float)
    ts = np.loadtxt(filename, delimiter=',', usecols=1, dtype=float)
    xs = np.loadtxt(filename, delimiter=',', usecols=(2, 3, 4, 5), dtype=float)
    data_len = len(weeks)

    plt.plot(weeks, ts, 'r')
    plt.show()
