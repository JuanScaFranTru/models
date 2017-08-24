#!/usr/bin/python3
"""Train a model

Usage:
  ./train.py -i <filename> -c <r> -e <r> -g <r>
  ./train.py -h | --help

Options:
  -i <filename> Instance filename (data)
  -c <r>        Number of classes to train [default: 6]
  -e <r>        Epsilon
  -g <r>        Gamma
  -h --help     Show this screen.
"""
from docopt import docopt
from models.utils import load_data, stats
from sklearn.svm import SVR


if __name__ == '__main__':
    opts = docopt(__doc__)

    # Read the penalty parameter
    C = float(opts['-c'])
    epsilon = float(opts['-e'])
    gamma = float(opts['-g'])

    filename = opts['-i']

    data_len, weeks, ts, xs = load_data(filename=filename)

    SVR_model = SVR(gamma=gamma, epsilon=epsilon, C=C, max_iter=2000)
    SVR_model.fit(xs, ts)

    mean, std_dev = stats(xs, ts, SVR_model)
    print(mean)
