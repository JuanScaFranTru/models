from sklearn.decomposition import PCA
from models.utils import load_data, plot_prediction, print_stats
from models.positive_models import PositiveLinearRegression


if __name__ == '__main__':
    n_components = 8

    data_len, weeks, ts, xs = load_data()

    means, std_devs = [], []

    pca = PCA(n_components=n_components)
    xs_pca = pca.fit(xs).transform(xs)

    linear_model = PositiveLinearRegression()
    linear_model.fit(xs_pca, ts)

    mean, std_dev = print_stats(xs_pca, ts, linear_model)
    plot_prediction(weeks, xs_pca, ts, linear_model)

    means.append(mean)
    std_devs.append(std_dev)
