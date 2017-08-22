"""3D Plot of the data. Each class is represented using a different
color.

Usage:
  train.py [-c <n>]
  train.py -h | --help

Options:
  -c <n>        Number of classes to train [default: 5]
  -o <file>     Output filename
  -h --help     Show this screen.

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from docopt import docopt
from models.utils import load_data, to_classes


if __name__ == '__main__':
    opts = docopt(__doc__)
    nclasses = int(opts['-c'])

    data_len, weeks, ts, xs = load_data()

    a, b, c = (1, 2, 3)
    x = xs[:, a]
    y = xs[:, b]
    z = xs[:, c]
    c = to_classes(ts, nclasses=nclasses)
    c = -c  # Reverse the colors

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c=c)
    plt.show()
