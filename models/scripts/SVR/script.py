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
from sklearn.svm import SVR
from models.utils import load_data, stats


if __name__ == '__main__':
    opts = docopt(__doc__)

    # Read the penalty parameter
    C = float(opts['-c'])
    filename = opts['-i']

    data_len, weeks, ts, xs = load_data(filename=filename)

    SVR_model = SVR(C=C)
    SVR_model.fit(xs, ts)

    _, mean, std_dev = stats(xs, ts, SVR_model)
    print(mean)
