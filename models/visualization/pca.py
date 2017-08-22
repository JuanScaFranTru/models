"""Plot a 3D PCA of the data. Each class is represented using a different
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
from sklearn.decomposition import PCA
from docopt import docopt
from models.utils import load_data, to_classes


if __name__ == '__main__':
    opts = docopt(__doc__)
    nclasses = int(opts['-c'])

    data_len, weeks, ts, xs = load_data()

    pca = PCA(n_components=3)
    xs_pca = pca.fit(xs).transform(xs)

    x = xs_pca[:, 0]
    y = xs_pca[:, 1]
    z = xs_pca[:, 2]
    c = to_classes(ts, nclasses=nclasses)
    c = -c  # Reverse the colors

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c=c)
    plt.show()
