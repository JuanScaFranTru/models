#!/usr/bin/python3
"""Train a model

Usage:
  ./train.py -i <filename> -c <n>
  ./train.py -h | --help

Options:
  -i <filename> Instance filename (data)
  -c <n>        Number of classes to train [default: 6]
  -h --help     Show this screen.
"""
from docopt import docopt
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR


def smoothing(xs):
    n = len(xs)
    for i in range(1, n - 1):
        xs[i] = sum([xs[j] for j in [i - 1, i, i + 1]]) / 3
    xs[0] = xs[1]
    xs[n - 1] = xs[n - 2]

    return xs


def load_data(cols=None, filename='Instaces/all_data.csv', split=None):
    """Load the training data set.
    Preconditions: 0 <= split <= 1

    split -- percentage of dataset (e.g. 0.9). If None, no splitting is done.
    """

    assert split is None or 0 <= split <= 1

    if cols is None:
        cols = tuple(range(2, 34))

    weeks = np.loadtxt(filename, delimiter=',', usecols=0, dtype=float)
    ts = np.loadtxt(filename, delimiter=',', usecols=1, dtype=float)
    xs = np.loadtxt(filename, delimiter=',', usecols=cols, dtype=float)
    data_len = len(weeks)

    ts = smoothing(ts)

    if split is None:
        return data_len, weeks, ts, xs
    else:
        # Reserve split * 100% of the data for validation
        split_point = int(data_len * split)
        ts, vts = ts[0:split_point], ts[split_point:data_len]
        xs, vxs = xs[0:split_point, :], xs[split_point:data_len, :]
        weeks, vweeks = weeks[0:split_point], weeks[split_point:data_len]
        return data_len, weeks, ts, xs, vweeks, vts, vxs


def stats(xs, ts, model, title='Stats', n_splits=5):
    cv = TimeSeriesSplit(n_splits)
    scores = cross_val_score(model, xs, ts, cv=cv.split(xs),
                             scoring='neg_mean_squared_error')
    scores = np.sqrt(-scores)
    mean = np.mean(scores)
    std_dev = np.std(scores)

    return mean, std_dev


if __name__ == '__main__':
    opts = docopt(__doc__)

    # Read the penalty parameter
    C = float(opts['-c'])
    filename = opts['-i']

    data_len, weeks, ts, xs = load_data(filename=filename)

    SVR_model = SVR(C=C)
    SVR_model.fit(xs, ts)

    mean, std_dev = stats(xs, ts, SVR_model)
    print(mean)
