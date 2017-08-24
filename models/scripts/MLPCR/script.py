#!/usr/bin/python3
"""Train a model
Usage:
  ./train.py -i <filename> -a <r> -n <n> -h <n>
  ./train.py -h | --help
Options:
  -i <filename> Instance filename (data)
  -a <r>        Alpha
  -n <n>        Neurons
  -h <n>        Hidden layers
  -h --help     Show this screen.
"""
from docopt import docopt
from models.utils import load_data, stats
from sklearn.neural_network import MLPRegressor


if __name__ == '__main__':
    opts = docopt(__doc__)

    # Read the penalty parameter
    alpha = float(opts['-a'])
    hidden = int(opts['-h'])
    neurons = int(opts['-n'])
    filename = opts['-i']

    data_len, weeks, ts, xs = load_data(filename=filename)

    MLPR_model = MLPRegressor(solver='lbfgs', activation='logistic', alpha=alpha)
    MLPR_model.fit(xs, ts)

    mean, std_dev = stats(xs, ts, MLPR_model)
