from sklearn.decomposition import PCA
from models.utils import load_data, plot_prediction, print_stats
from models.positive_models import PositiveRidgeCV


if __name__ == '__main__':
    n_components = 8

    data_len, weeks, ts, xs = load_data()

    pca = PCA(n_components=n_components)
    xs_pca = pca.fit(xs).transform(xs)

    ridge_model = PositiveRidgeCV()
    ridge_model.fit(xs_pca, ts)

    print_stats(xs_pca, ts, ridge_model)
    plot_prediction(weeks, xs_pca, ts, ridge_model)
