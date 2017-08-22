import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from models.positive_models import PositiveLinearRegression
from models.utils import load_data, print_stats


if __name__ == '__main__':
    data_len, weeks, ts, xs = load_data()

    means, std_devs = [], []

    n_components = list(range(1, 33))
    for i in n_components:
        title = 'Number of components of PCA: {}'.format(i)
        print(title)
        print('-' * len(title))

        pca = PCA(n_components=i)
        xs_pca = pca.fit(xs).transform(xs)

        linear_model = PositiveLinearRegression()
        linear_model.fit(xs_pca, ts)

        mean, std_dev = print_stats(xs_pca, ts, linear_model)

        means.append(mean)
        std_devs.append(std_dev)

    plt.plot(n_components, means, label='mean of scores')
    plt.plot(n_components, std_devs, label='std dev of scores')
    plt.xlabel('Number of PCA components')
    plt.legend()
    plt.show()
