from sklearn.linear_model import RidgeCV
from models.utils import load_data, plot_prediction, print_stats


if __name__ == '__main__':
    data_len, weeks, ts, xs = load_data()

    linear_model = RidgeCV()
    linear_model.fit(xs, ts)

    print_stats(xs, ts, linear_model)
    plot_prediction(weeks, xs, ts, linear_model)
